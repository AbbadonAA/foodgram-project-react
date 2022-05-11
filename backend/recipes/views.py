from rest_framework import viewsets

from recipes.models import Recipe
from recipes.serializers import RecipeGetSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeGetSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
