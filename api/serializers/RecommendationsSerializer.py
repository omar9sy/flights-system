from api.models import Hotel, Restaurant
from rest_framework import serializers


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class ResultSerializer(serializers.Serializer):
    hotels = HotelSerializer(read_only=True)
    restaurants = RestaurantSerializer(read_only=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
