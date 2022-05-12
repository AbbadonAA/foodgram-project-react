from drf_base64.fields import Base64ImageField
from rest_framework import serializers

from recipes.models import Recipe, IngredientAmount
from tags_ingr.serializers import TagSerializer
from users.serializers import CustomUserSerializer


class IngredientAmountGetSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='ingredient.name')
    measurement_unit = serializers.ReadOnlyField(
        source='ingredient.measurement_unit')

    class Meta:
        model = IngredientAmount
        fields = (
            'id', 'name', 'measurement_unit', 'amount'
        )


class RecipeGetSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    ingredients = IngredientAmountGetSerializer(
        many=True, read_only=True, source='ingredientamount_set')
    image = Base64ImageField()

    class Meta:
        model = Recipe
        fields = (
            'id', 'tags', 'author', 'ingredients', 'name',
            'image', 'text', 'cooking_time'
        )


# class RecipePostSerializer(serializers.ModelSerializer):
#     author = serializers.SlugRelatedField(
#         slug_field='username', read_only=True, default=''
#     )
#     tags = serializers.SlugRelatedField(
#         many=True, queryset=Tag.objects.all(), slug_field='id'
#     )
#     ingredients = IngredientAmountPostSerializer(many=True)
#     image = Base64ImageField()

#     class Meta:
#         model = Recipe
#         fields = (
#             'id', 'ingredients', 'tags', 'author', 'name',
#             'image', 'text', 'cooking_time'
#         )

#     def create(self, validated_data):
#         ingredients_data = validated_data.pop('ingredients')
#         recipe = Recipe.objects.create(**validated_data)
#         for ingredient in ingredients_data:
#             IngredientAmount.objects.create(recipe=recipe, **ingredient)
#         return recipe
