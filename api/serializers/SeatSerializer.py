from api.models import Seat
from rest_framework import serializers


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
