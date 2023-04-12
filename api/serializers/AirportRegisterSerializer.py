from api.models import AppUser, Airport
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction
from rest_framework import serializers


class AirportRegisterSerializer(RegisterSerializer):
    phone_number = serializers.CharField(max_length=11, required=False)
    country = serializers.CharField(max_length=20, required=False)
    city = serializers.CharField(max_length=20, required=False)
    email = serializers.EmailField(required=True)
    name = serializers.CharField(max_length=20, required=False)
    photo = serializers.ImageField(required=False)

    class Meta:
        model = AppUser
        fields = (
            'email',
            'phone_number',
            'country',
            'city',
            'first_name',
            'last_name',
            'photo'
        )

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.phone_number = self.data.get('phone_number')
        user.city = self.data.get('city')
        user.country = self.data.get('country')
        user.first_name = self.data.get('first_name', 'airport')
        user.last_name = self.data.get('last_name', 'airport')
        user.is_airport = True
        user.save()
        airport = Airport(author=user, name=self.data.get('name'),
                          city=user.city, country=user.country)
        airport.save()
        airport.photo = self.data.get('photo')
        airport.save()
        return user
