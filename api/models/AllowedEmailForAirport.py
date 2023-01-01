from django.db import models


class AllowedEmailForAirport(models.Model):
    Email = models.EmailField()
