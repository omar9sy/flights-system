from django.db import models
from . import Airport


class Trip(models.Model):
    departure_date = models.DateField()
    departure_time = models.TimeField()

    arrival_date = models.DateField()
    arrival_time = models.TimeField()

    destination_country = models.CharField(max_length=50)
    destination_city = models.CharField(max_length=50)

    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='trips')
