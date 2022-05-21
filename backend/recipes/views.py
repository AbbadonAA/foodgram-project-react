# from django.core.files import File
# from django.http import FileResponse
# from django.utils.http import urlquote

from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from fpdf import FPDF
from recipes.filters import RecipeFilter
from recipes.models import Favorite, IngredientAmount, Recipe, ShoppingCart
from recipes.serializers import RecipeSerializer, SmallRecipeSerializer
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    http_method_names = [
        'get', 'post', 'patch', 'delete', 'head', 'options']
    filter_backends = (DjangoFilterBackend,)
    filter_class = RecipeFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def update(self, request, *args, **kwargs):
        """Запрет частичного обновления."""
        kwargs['partial'] = False
        return super().update(request, *args, **kwargs)

    @action(methods=['post'], detail=True, url_path='favorite',
            url_name='favorite')
    def favorite(self, request, pk=None):
        """Добавление рецептов в избранное."""
        user = request.user
        recipe = get_object_or_404(Recipe, pk=pk)
        favorite = Favorite.objects.filter(user=user, recipe=recipe).exists()
        if favorite:
            return Response(
                {'errors': 'Нельзя повторно добавить рецепт в избранное'},
                status=status.HTTP_400_BAD_REQUEST
            )
        Favorite.objects.create(user=user, recipe=recipe)
        serializer = SmallRecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @favorite.mapping.delete
    def delete_favorite(self, request, pk=None):
        """Удаление рецепта из избранного."""
        user = request.user
        recipe = get_object_or_404(Recipe, pk=pk)
        favorite = Favorite.objects.filter(user=user, recipe=recipe)
        if not favorite.exists():
            return Response(
                {'errors': 'Нельзя повторно удалить рецепт из избранного'},
                status=status.HTTP_400_BAD_REQUEST
            )
        favorite.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True, url_path='shopping_cart',
            url_name='shopping_cart')
    def shopping_cart(self, request, pk=None):
        """Добавление рецептов в избранное."""
        user = request.user
        recipe = get_object_or_404(Recipe, pk=pk)
        cart = ShoppingCart.objects.filter(user=user, recipe=recipe).exists()
        if cart:
            return Response(
                {'errors': 'Нельзя повторно добавить рецепт в список покупок'},
                status=status.HTTP_400_BAD_REQUEST
            )
        ShoppingCart.objects.create(user=user, recipe=recipe)
        serializer = SmallRecipeSerializer(recipe)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @shopping_cart.mapping.delete
    def delete_shopping_cart(self, request, pk=None):
        """Удаление рецепта из избранного."""
        user = request.user
        recipe = get_object_or_404(Recipe, pk=pk)
        cart = ShoppingCart.objects.filter(user=user, recipe=recipe)
        if not cart.exists():
            return Response(
                {'errors': 'Нельзя повторно удалить рецепт из списка покупок'},
                status=status.HTTP_400_BAD_REQUEST
            )
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['get'], detail=False, url_path='download_shopping_cart',
            url_name='download_shopping_cart')
    def download_cart(self, request):
        """Формирование и скачивание списка покупок."""
        user = request.user
        ingredients = IngredientAmount.objects.filter(
            recipe__sh_cart__user=user).values(
                'ingredient__name', 'ingredient__measurement_unit').annotate(
                    Sum('amount', distinct=True))
        lines = []
        for ingredient in ingredients:
            name = ingredient['ingredient__name']
            unit = ingredient['ingredient__measurement_unit']
            amount = ingredient['amount__sum']
            lines.append(f'{name} - {amount} {unit}')
        data = '\n'.join(lines)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("helvetica", "B", 16)
        pdf.cell(40, 10, data)
        file = pdf.output('shopping_cart.pdf')
        response = HttpResponse(
            content_type='application/pdf', status=status.HTTP_200_OK)
        response['Content-Disposition'] = (
            'attachment; filename="shopping_cart.pdf"')
        response.write(file)
        return response

        # response = HttpResponse(
        #     content_type='text/plain', status=status.HTTP_200_OK)
        # response['Content-Disposition'] = (
        #     'attachment; filename="shopping_cart.txt"')
        # response.write('Список покупок:' + '\n\n')
        # for ingredient in ingredients:
        #     name = ingredient['ingredient__name']
        #     unit = ingredient['ingredient__measurement_unit']
        #     amount = ingredient['amount__sum']
        #     response.write(f'{name} - {amount} {unit}' + '\n')
        # return response
