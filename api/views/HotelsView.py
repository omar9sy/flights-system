from api.models import Hotel, Restaurant
from api.serializers import HotelSerializer, RestaurantSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_hotels_and_restaurants(request):
    hotels = HotelSerializer(Hotel.objects.all(), many=True)
    restaurants = RestaurantSerializer(Restaurant.objects.all(), many=True)
    return Response({'hotels': hotels.data, 'restaurants': restaurants.data})
