from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(max_length=63, null=True, blank=True)
