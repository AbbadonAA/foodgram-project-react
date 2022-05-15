from django_filters import ModelMultipleChoiceFilter
from django_filters.rest_framework import FilterSet
from recipes.models import Recipe
from tags_ingr.models import Tag


class TagRecipeFilter(FilterSet):
    tags = ModelMultipleChoiceFilter(
        field_name='tags__slug',
        to_field_name='slug',
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Recipe
        fields = (
            'tags',
        )
