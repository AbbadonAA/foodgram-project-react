from django_filters import ModelMultipleChoiceFilter
from django_filters.rest_framework import FilterSet, filters
from recipes.models import Recipe
from tags_ingr.models import Tag
from users.models import User


class RecipeFilter(FilterSet):
    tags = ModelMultipleChoiceFilter(
        field_name='tags__slug',
        to_field_name='slug',
        queryset=Tag.objects.all()
    )
    author = filters.ModelChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = Recipe
        fields = ('tags', 'author')
