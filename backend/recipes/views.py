from django_filters.rest_framework import DjangoFilterBackend
from recipes.filters import TagRecipeFilter
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer
from rest_framework import viewsets


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    http_method_names = ['get', 'post', 'patch', 'head', 'options']
    filter_backends = (DjangoFilterBackend,)
    filter_class = TagRecipeFilter

    # filter_backends = [filters.SearchFilter]
    # search_fields = ('^ingredient__name',)

    # search_nested_fields = {
    #     'ingredients': {
    #         'path': 'ingredients',
    #         'fields': ['^name'],
    #     }
    # }

    # def get_serializer_class(self):
    #     if self.action == 'list' or self.action == 'retrieve':
    #         return RecipeGetSerializer
    #     if self.action == 'create':
    #         return RecipePostSerializer
    #     return RecipeGetSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
