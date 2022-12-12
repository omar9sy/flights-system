from api.models import Trip, Seat, TripReservation, Airport
from api.permissions import IsAirport
from api.serializers import TripSerializer, TripCreateSerializer
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
    # return Response(serializer.data)
    airport = Airport.objects.filter(author=request.user).first()
    # return Response(airport.id)
    data = serializer.data
    trip = Trip.objects.create(
        departure_date=data.get('departure_date'),
        departure_time=data.get('departure_time'),
        arrival_date=data.get('arrival_date'),
        arrival_time=data.get('arrival_time'),
        destination_country=data.get('destination_country'),
        destination_city=data.get('destination_city'),
        airport=airport
    )
    trip.save()
    for i in range(10):
        obj = Seat.objects.create(trip=trip, level=1, cost=data.get('level_1_cost'))
        obj.save()

    for i in range(20):
        obj = Seat.objects.create(trip=trip, level=2, cost=data.get('level_2_cost'))
        obj.save()

    for i in range(30):
        obj = Seat.objects.create(trip=trip, level=2, cost=data.get('level_3_cost'))
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def book_seat(request, pk, seat_id):
    seat = get_object_or_404(Seat, pk=seat_id)
    if seat.booked:
        return Response({'message': 'this seat is booked'}, status=status.HTTP_400_BAD_REQUEST)

    user = request.user
    trip = get_object_or_404(Trip, pk=pk)
    obj = TripReservation.objects.create(trip=trip, seat=seat, user=user, cost=seat.get_offer_cost)
    obj.save()
    seat.booked = True
    seat.save()
    return Response({'message': 'seat booked'}, status=status.HTTP_201_CREATED)
