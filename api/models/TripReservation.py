from api.models import AppUser, Trip, Seat
from django.db import models


class TripReservation(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='user_reservations')
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='trip_reservations')
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE,related_name='seat')
    cost = models.IntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ' to ' + str(self.trip)
