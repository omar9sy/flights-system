from api.models import Airport, Trip
from rest_framework import serializers


class AirportTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


class AirportSerializer(serializers.ModelSerializer):
    trips = AirportTripSerializer(many=True,read_only=True)

    class Meta:
        model = Airport
        fields = ['id', 'name', 'city', 'country', 'trips']