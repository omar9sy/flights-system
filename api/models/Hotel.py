from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    price = models.IntegerField()
    rate = models.IntegerField()
