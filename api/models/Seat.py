from django.db import models
from django.utils.datetime_safe import datetime

from . import Trip


class Seat(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='seats')
    level = models.IntegerField()
    booked = models.BooleanField(default=False)
    cost = models.IntegerField()

    def __str__(self) -> str:
        return str(self.pk) + ' booked:'+str(self.booked)

    @property
    def get_offer_cost(self):
        cur_date = datetime.now().date()
        dep_date = datetime.strptime(str(self.trip.departure_date), '%Y-%m-%d').date()
        # print(dep_date)
        diff = cur_date - dep_date

        discount = 1.0

        if diff.days > 30:
            discount = 0.75
        elif diff.days > 20:
            discount = 0.85
        elif diff.days >= 0:
            discount = 0.95

        return self.cost * discount
