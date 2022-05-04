from django.contrib.auth.models import AbstractUser
# from django.contrib.auth import get_user_model
from django.db import models

# User = get_user_model()


class User(AbstractUser):
    email = models.EmailField(
        max_length=254,
        unique=True,
    )
    username = models.CharField(
        max_length=150,
        unique=True,
    )
    first_name = models.CharField(
        max_length=150,
    )
    last_name = models.CharField(
        max_length=150,
    )
    password = models.CharField(
        max_length=150,
    )

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.username
