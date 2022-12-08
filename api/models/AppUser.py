from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class AppUser(AbstractUser):
    phone_number = models.CharField(max_length=11)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
