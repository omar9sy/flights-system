from django.apps import AppConfig
from django.core.mail import send_mail
from django.utils.datetime_safe import datetime


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def send(self, user, trip):
        send_mail(
            'reminder of flight',
            f'you have a flight at {trip.departure_date}',
            'flightsmanager5@gmail.com',
            [user.email],
            fail_silently=False,
        )

    def ready(self):
        from .models import TripReservation

        print('test')
        data = TripReservation.objects.all()
        for reservation in data:
            data = datetime.now().date()
            diff = reservation.trip.departure_date - data
            if diff.days <= 2:
                print(reservation.user.email)
                self.send(reservation.user, reservation.trip)
