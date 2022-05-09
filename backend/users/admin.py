from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
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


admin.site.register(User, CustomUserAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
