from django.db import models
from .Trip import *


class Seat(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='seats')
    level = models.IntegerField()
    row = models.IntegerField()
    numer = models.IntegerField()
    booked = models.BooleanField(default=False)
