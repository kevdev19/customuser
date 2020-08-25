from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
    displayname = models.CharField(max_length=60, unique=True, null=False)
    # additional fields will go here

    def __str__(self):
        return self.username
