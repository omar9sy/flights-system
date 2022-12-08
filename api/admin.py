from api.models import AppUser, Airport, Trip, Seat
from django.contrib import admin

# Register your models here.
admin.site.register(AppUser)
admin.site.register(Airport)
admin.site.register(Trip)
admin.site.register(Seat)
