from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
    # displayname = models.CharField(max_length=60, unique=True, null=False)
    displayname = models.CharField(max_length=60, null=False)
    age = models.IntegerField(null=True, blank=True)
    homepage = models.URLField(max_length=100, null=True, blank=True)

    REQUIRED_FIELDS = ['age', 'homepage']

    def __str__(self):
        return self.username
