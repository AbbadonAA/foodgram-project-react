from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from recipes.models import Recipe
from tags_ingr.models import Ingredient, Tag

from .models import User


class CustomUserAdmin(UserAdmin):
    """Кастомная админка для модели User."""
    search_fields = ('email', 'username')
    list_filter = ('email', 'username')
    ordering = ('pk',)


class IngredientAdmin(admin.ModelAdmin):
    """Кастомная админка для модели Ingredient."""
    list_display = (
        'pk',
        'name',
        'measurement_unit',
    )
    list_editable = ('name', 'measurement_unit')
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class TagAdmin(admin.ModelAdmin):
    """Кастомная админка для модели Tag."""
    list_display = (
        'pk',
        'name',
        'color',
        'slug',
    )
    list_editable = ('name', 'color', 'slug')
    search_fields = ('name',)
    empty_value_display = '-пусто-'


# class RecipeAdmin(admin.ModelAdmin):
#     """Кастомная админка для модели Recipe."""
#     list_display = (
#         'pk',
#         'pub_date',
#         'tags',
#         'author',
#         'ingredients',
#         'image',
#         'text',
#         'cooking_time'
#     )
#     search_fields = ('name', 'text', 'ingredients', 'author')
#     list_filter = ('tags',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
# admin.site.register(Recipe, RecipeAdmin)
