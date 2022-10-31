from django.db import models
from django.contrib.auth.models import AbstractUser

class Thing(AbstractUser):
    name = models.CharField()
    descirption = models.CharField()
    quantity = models.IntegerField()
