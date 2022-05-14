from django.core.exceptions import ValidationError
from rest_framework.validators import ValidationError as RFError
from tags_ingr.models import Ingredient, Tag


def validate_time(value):
    if value < 1:
        raise ValidationError(
            'Время приготовления не может быть меньше минуты.'
        )


def validate_ingredients(data):
    if len(data) < 1:
        raise RFError('Не переданы ингредиенты')
    unique_ingredient = []
    for ingredient in data:
        if not ingredient.get('id'):
            raise RFError('Отсутствует id ингредиента')
        if not ingredient.get('amount'):
            raise RFError('Количество не может быть менее 1')
        id = ingredient.get('id')
        if not Ingredient.objects.filter(id=id).exists():
            raise RFError('Некорректный ингредиент - отсутствует в БД')
        if id in unique_ingredient:
            raise RFError('Нельзя дублировать имена ингредиентов')
        unique_ingredient.append(id)
        amount = int(ingredient.get('amount'))
        if amount < 1:
            raise RFError('Количество не может быть менее 1')
    return data


def validate_tags(data):
    if len(data) < 1:
        raise RFError('Хотя бы один тэг должен быть указан')
    for tag in data:
        if not Tag.objects.filter(id=tag).exists():
            raise RFError('Некорректный тэг - отсутствует в БД')
    return data
