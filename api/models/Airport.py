from api.helpers import upload_to
from api.models import AppUser
from django.db import models


class Airport(models.Model):
    author = models.ForeignKey(AppUser, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=upload_to, null=True, blank=True)

    def __str__(self):
        return self.name
