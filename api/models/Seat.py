from django.db import models
from . import Trip


class Seat(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='seats')
    level = models.IntegerField()
    row = models.IntegerField()
    number = models.IntegerField()
    booked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(self.level)+' '+str(self.row)+' '+str(self.number) + ' booked:'+str(self.booked)
