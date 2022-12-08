from api.models import Trip, Seat
from rest_framework import serializers


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = [
            'id',
            'level',
            'row',
            'numer',
            'booked',
        ]


class TripSerializer(serializers.ModelSerializer):
    seats = SeatSerializer(many=True, read_only=True)

    class Meta:
        model = Trip
        fields = [
            'departure_date',
            'departure_time',
            'arrival_date',
            'arrival_time',
            'destination_country',
            'destination_city',
            'seats'
        ]
