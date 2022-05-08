from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tags_ingr.models import Ingredient, Tag

from .models import User

admin.site.register(User, UserAdmin)
admin.site.register(Tag)
admin.site.register(Ingredient)
