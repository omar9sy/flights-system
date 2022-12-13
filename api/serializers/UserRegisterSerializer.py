from api.models import AppUser
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction
from rest_framework import serializers


class UserRegisterSerializer(RegisterSerializer):
    phone_number = serializers.CharField(max_length=11, required=False)
    country = serializers.CharField(max_length=20, required=False)
    city = serializers.CharField(max_length=20, required=False)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField(required=True)

    class Meta:
        model = AppUser
        fields = (
            'email',
            'phone_number',
            'country',
            'city',
            'first_name',
            'last_name'
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
        user.first_name = self.data.get('first_name')
        user.first_name = self.data.get('last_name')
        user.save()
        return user
