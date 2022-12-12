from api.models import AppUser
from django.db import models


class Comment(models.Model):
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(AppUser, on_delete=models.CASCADE)
