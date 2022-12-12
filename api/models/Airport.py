from api.models import AppUser
from django.db import models


class Airport(models.Model):
    author = models.ForeignKey(AppUser, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name
