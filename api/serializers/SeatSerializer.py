from api.models import Seat
from rest_framework import serializers


class SeatSerializer(serializers.ModelSerializer):
    offer_cost = serializers.DecimalField(source='get_offer_cost', read_only=True,
                                          max_digits=12, decimal_places=2)

    class Meta:
        model = Seat
        fields = [
            'id',
            'level',
            'booked',
            'cost',
            'offer_cost'
        ]
