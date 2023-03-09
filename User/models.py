from django.db import models
from django.contrib.auth.models import *


class Profil(models.Model):
    ism = models.CharField(max_length=30)
    jins = models.CharField(max_length=10)
    shaxar = models.CharField(max_length=50)
    mamlakat = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.ism

