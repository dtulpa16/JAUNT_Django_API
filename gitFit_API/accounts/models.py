from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_employee = models.BooleanField(default=False)
    age = models.IntegerField(null=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    goal = models.CharField(max_length=75,null=True)
    calories = models.IntegerField(null=True)
    gender = models.CharField(max_length=15,null=True)