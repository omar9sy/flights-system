from api.models import AllowedEmailForAirport
from rest_framework import serializers


class AllowedEmailForAirportSerializer(serializers.ModelSerializer):

    class Meta:
        model = AllowedEmailForAirport
        fields = ['Email']
