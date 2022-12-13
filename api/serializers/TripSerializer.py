from api.models import Trip, TripReservation
from rest_framework import serializers
from . import SeatSerializer


class TripSerializer(serializers.ModelSerializer):
    seats = SeatSerializer(many=True, read_only=True)

    class Meta:
        model = Trip
        fields = [
            'id',
            'departure_date',
            'departure_time',
            'arrival_date',
            'arrival_time',
            'destination_country',
            'destination_city',
            'seats'
        ]


class TripCreateSerializer(serializers.Serializer):
    level_1_cost = serializers.IntegerField()
    level_2_cost = serializers.IntegerField()
    level_3_cost = serializers.IntegerField()
    departure_date = serializers.DateField()
    departure_time = serializers.TimeField()
    arrival_date = serializers.DateField()
    arrival_time = serializers.TimeField()
    destination_country = serializers.CharField()
    destination_city = serializers.CharField()

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class TripRSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = [
            'id',
            'departure_date',
            'departure_time',
            'arrival_date',
            'arrival_time',
            'destination_country',
            'destination_city'
        ]


class TripReservationSerializer(serializers.ModelSerializer):
    # user = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='user_reservations')
    # trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='trip_reservations')
    # seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='seat')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    trip = TripRSerializer(read_only=True)

    class Meta:
        model = TripReservation
        fields = ['cost', 'booked_at', 'first_name',
                  'last_name', 'trip'
                  ]
