from api.models import Trip, Seat
from rest_framework import serializers
from datetime import datetime

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = [
            'id',
            'level',
            'row',
            'number',
            'booked',
        ]


class TripSerializer(serializers.ModelSerializer):
    seats = SeatSerializer(many=True, read_only=True)
    offer_cost = serializers.DecimalField(source='get_offer_cost', read_only=True, 
    max_digits=12, decimal_places=2)

    class Meta:
        model = Trip
        fields = [
            'departure_date',
            'departure_time',
            'arrival_date',
            'arrival_time',
            'destination_country',
            'destination_city',
            'seats',
            'cost',
            'offer_cost'
        ]

