from api.models import AppUser, Airport, Trip, Seat, TripReservation, Restaurant, Hotel
from django.contrib import admin

# Register your models here.
admin.site.register(AppUser)
admin.site.register(Airport)
admin.site.register(Trip)
admin.site.register(Seat)
admin.site.register(TripReservation)
admin.site.register(Hotel)
admin.site.register(Restaurant)
