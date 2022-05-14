from django.shortcuts import get_object_or_404
from drf_base64.fields import Base64ImageField
from recipes.models import IngredientAmount, Recipe
from recipes.validators import validate_ingredients, validate_tags
from rest_framework import serializers
from tags_ingr.models import Ingredient, Tag
from tags_ingr.serializers import TagSerializer
from users.serializers import CustomUserSerializer


class IngredientAmountSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='ingredient.id')
    name = serializers.ReadOnlyField(source='ingredient.name')
    measurement_unit = serializers.ReadOnlyField(
        source='ingredient.measurement_unit')

    class Meta:
        model = IngredientAmount
        fields = (
            'id', 'name', 'measurement_unit', 'amount'
        )


class RecipeSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    ingredients = IngredientAmountSerializer(
        read_only=True, many=True, source='ingredientamount_set')
    image = Base64ImageField()

    class Meta:
        model = Recipe
        fields = (
            'id', 'tags', 'author', 'ingredients', 'name',
            'image', 'text', 'cooking_time'
        )

    def create(self, validated_data):
        ingredients_data = self.initial_data.get('ingredients')
        valid_ingredients = validate_ingredients(ingredients_data)
        recipe = Recipe.objects.create(**validated_data)
        tags_id = self.initial_data.get('tags')
        valid_tags = validate_tags(tags_id)
        tags = Tag.objects.filter(id__in=valid_tags)
        recipe.tags.set(tags)
        for ingredient_data in valid_ingredients:
            ingredient = get_object_or_404(
                Ingredient, id=ingredient_data.get('id'))
            IngredientAmount.objects.create(
                recipe=recipe,
                ingredient=ingredient,
                amount=ingredient_data.get('amount'))
        return recipe


# class RecipePostSerializer(serializers.ModelSerializer):
#     author = CustomUserSerializer(read_only=True)
#     tags = TagSerializer(read_only=True, many=True)
#     ingredients = IngredientAmountGetSerializer(
#         read_only=True, many=True, source='ingredientamount_set')
#     image = Base64ImageField()

#     class Meta:
#         model = Recipe
#         fields = (
#             'id', 'tags', 'author', 'ingredients', 'name',
#             'image', 'text', 'cooking_time'
#         )

#     def create(self, validated_data):
#         ingredients_data = self.initial_data.get('ingredients')
#         recipe = Recipe.objects.create(**validated_data)
#         tags_id = self.initial_data.get('tags')
#         tags = Tag.objects.filter(id__in=tags_id)
#         recipe.tags.set(tags)
#         for ingredient_data in ingredients_data:
#             ingredient = get_object_or_404(
#                 Ingredient, id=ingredient_data.get('id'))
#             IngredientAmount.objects.create(
#                 recipe=recipe,
#                 ingredient=ingredient,
#                 amount=ingredient_data.get('amount'))
#         return recipe
