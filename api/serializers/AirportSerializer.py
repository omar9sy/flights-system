from api.models import Airport, Trip
from rest_framework import serializers


class AirportTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


class AirportSerializer(serializers.ModelSerializer):
    trips = AirportTripSerializer(many=True, read_only=True)
    photo_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Airport
        fields = ['id', 'name', 'city', 'country', 'trips', 'photo_url']

    def get_photo_url(self, instance) -> str:
        request = self.context.get('request')
        try:
            photo_url = instance.photo.url
            return request.build_absolute_uri(photo_url)
        except:
            return "NO Photo"


class AirporCreatetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airport
        fields = ['id', 'name', 'city', 'country', 'photo']

    def create(self, validated_data):
        photo = validated_data.pop('photo', None)
        instance = super().create(validated_data)
        instance.save()
        instance.photo = photo
        instance.save()
        return instance
