import decimal
from api.models import Trip, Seat, TripReservation, Airport, AppUser, Restaurant, Hotel
from api.permissions import IsAirport
from api.serializers import TripSerializer, TripCreateSerializer, TripReservationSerializer, RestaurantSerializer, \
    HotelSerializer, ResultSerializer
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@extend_schema(
    request=TripCreateSerializer,
    responses=TripCreateSerializer
)
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAirport])
def create_trip(request):
    serializer = TripCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    airport = Airport.objects.filter(author=request.user).first()
    data = serializer.data
    costs = [data.pop('level_1_cost'), data.pop('level_2_cost'), data.pop('level_3_cost')]

    trip = Trip.objects.create(**data, airport=airport)
    trip.save()
    for i in range(10):
        obj = Seat.objects.create(trip=trip, level=1, cost=costs[0])
        obj.save()

    for i in range(20):
        obj = Seat.objects.create(trip=trip, level=2, cost=costs[1])
        obj.save()

    for i in range(30):
        obj = Seat.objects.create(trip=trip, level=2, cost=costs[2])
        obj.save()

    result = TripSerializer(trip)
    return Response({'result': result.data}, status=status.HTTP_201_CREATED)


@extend_schema(
    responses=TripSerializer
)
@api_view(['GET'])
def get_trip(request, pk):
    obj = get_object_or_404(Trip, pk=pk)
    serializer = TripSerializer(obj)
    return Response({'result': serializer.data})


@extend_schema(
    responses=TripSerializer
)
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_user_trips(request):
    user = request.user
    data = TripReservation.objects.filter(user=user)
    serializer = TripReservationSerializer(data, many=True)
    return Response({'result': serializer.data})


@extend_schema(
    responses=TripSerializer
)
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAirport])
def get_airport_trip_reservations(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    data = TripReservation.objects.filter(trip=trip)
    serializer = TripReservationSerializer(data, many=True)
    return Response({'result': serializer.data})


@extend_schema(
    responses=ResultSerializer
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def book_seat(request, pk, seat_id):
    seat = get_object_or_404(Seat, pk=seat_id)
    if seat.booked:
        return Response({'message': 'this seat is booked'}, status=status.HTTP_400_BAD_REQUEST)

    user = AppUser.objects.get(pk=request.user.id)
    trip = get_object_or_404(Trip, pk=pk)
    if user.balance < seat.get_offer_cost:
        return Response({'error': 'insufficient balance'}, status=status.HTTP_400_BAD_REQUEST)

    obj = TripReservation.objects.create(trip=trip, seat=seat, user=user, cost=seat.get_offer_cost)
    obj.save()
    seat.booked = True
    seat.save()
    user.balance -= decimal.Decimal(seat.get_offer_cost)
    user.save()
    cnt = TripReservation.objects.filter(user=user).count()
    if cnt >= 3:
        restaurants = Restaurant.objects.filter(city=trip.destination_city).all()
        restaurants_serializer = RestaurantSerializer(restaurants, many=True)

        hotels = Hotel.objects.filter(city=trip.destination_city).all()
        hotels_serializer = HotelSerializer(hotels, many=True)

        return Response({'hotels': hotels_serializer.data, 'restaurants': restaurants_serializer.data})

    return Response({'message': 'seat booked'}, status=status.HTTP_201_CREATED)
