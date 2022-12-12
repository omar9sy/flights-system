import os

from django.utils import timezone


def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    return f"Airports/{instance.pk}/{now:%d%m%Y%H%M%S}{extension}"
