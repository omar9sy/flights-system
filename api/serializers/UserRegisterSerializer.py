from api.models import AppUser
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction
from rest_framework import serializers


class UserRegisterSerializer(RegisterSerializer):
    phone_number = serializers.CharField(max_length=11, required=False)
    country = serializers.CharField(max_length=20, required=False)
    city = serializers.CharField(max_length=20, required=False)

    class Meta:
        model = AppUser
        fields = (
            'name',
            'email',
            'password1',
            'password2',
            'phone_number',
            'country',
            'city'
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
        user.save()
        return user
