from api.models import Trip
from rest_framework import serializers
from . import SeatSerializer


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


class BookTripSerializer(serializers.Serializer):
    seat_id = serializers.IntegerField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
