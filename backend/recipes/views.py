from recipes.models import Recipe
from recipes.serializers import RecipeSerializer
from rest_framework import viewsets


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    # def get_serializer_class(self):
    #     if self.action == 'list' or self.action == 'retrieve':
    #         return RecipeGetSerializer
    #     if self.action == 'create':
    #         return RecipePostSerializer
    #     return RecipeGetSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
