from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class AppUser(AbstractUser):
    phone_number = models.CharField(max_length=11)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    is_airport = models.BooleanField(default=False)

    def __str__(self):
        return self.get_full_name() if self.get_full_name() != '' else self.username
