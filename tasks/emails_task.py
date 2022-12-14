from api.models import TripReservation
from django.core.mail import send_mail
from django.utils.datetime_safe import datetime


def send(user, trip):
    send_mail(
        'reminder of flight',
        f'''
        this is a reminder that you have a flight
        flight details
        date: {trip.departure_date}
        time: {trip.departure_time}                
        ''',
        'flightsmanager5@gmail.com',
        [user.email],
        fail_silently=False,
    )


def run():
    data = TripReservation.objects.all()
    for reservation in data:
        data = datetime.now().date()
        diff = reservation.trip.departure_date - data
        if diff.days <= 1:
            print(reservation.user.email)
            send(reservation.user, reservation.trip)
