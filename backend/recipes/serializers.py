from drf_base64.fields import Base64ImageField
from rest_framework import serializers

from recipes.models import Recipe, IngredientAmount
from tags_ingr.serializers import TagSerializer  # IngredientSerializer,
from users.serializers import CustomUserSerializer
from tags_ingr.models import Ingredient


class IngredientAmountSerializer(serializers.ModelSerializer):
    amount = serializers.SerializerMethodField('get_ingredient_amount')

    class Meta:
        model = Ingredient
        fields = (
            'id', 'name', 'measurement_unit', 'amount'
        )

    def get_ingredient_amount(self, obj):
        return IngredientAmount.objects.get(ingredients=obj).quantity


class RecipeGetSerializer(serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    ingredients = IngredientAmountSerializer(many=True, read_only=True)
    image = Base64ImageField()

    class Meta:
        model = Recipe
        fields = (
            'id', 'tags', 'author', 'ingredients', 'name',
            'image', 'text', 'cooking_time'
        )


# class RecipePostSerializer(serializers.ModelSerializer):
#     author = CustomUserSerializer()
#     tags = TagSerializer(many=True)
#     ingredients = IngredientSerializer(many=True)
#     image = Base64ImageField()

#     class Meta:
#         model = Recipe
#         fields = (
#             'id', 'tags', 'author', 'ingredients', 'name',
#             'image', 'text', 'cooking_time'
#         )
#         read_only_fields = ['author']
