from api.models import TripReservation
from django.core.mail import send_mail
from django.utils.datetime_safe import datetime


def send(user):
    send_mail(
        'Subject here',
        'Here is the message.',
        'flightsmanager5@gmail.com',
        [user.email],
        fail_silently=False,
    )


def run():
    print('test')
    data = TripReservation.objects.all()
    for reservation in data:
        data = datetime.now().date()
        diff = reservation.trip.departure_date - data
        if diff.days <= 2:
            print(reservation.user.email)
            send(reservation.user)
