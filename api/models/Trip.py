from django.db import models
from django.utils.datetime_safe import datetime

from . import Airport


class Trip(models.Model):
    departure_date = models.DateField()
    departure_time = models.TimeField()

    arrival_date = models.DateField()
    arrival_time = models.TimeField()

    destination_country = models.CharField(max_length=50)
    destination_city = models.CharField(max_length=50)

    cost = models.IntegerField()
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='trips')

    def __str__(self):
        return self.destination_city

    @property
    def get_offer_cost(self):
        cur_date = datetime.now().date()
        diff = cur_date - self.departure_date
        
        discount = 1.0

        if diff.days > 30:
            discount = 0.75
        elif diff.days > 20:
            discount = 0.85
        else:
            #diff.days > 10:
            discount = 0.95
        
        return self.cost*discount

        
