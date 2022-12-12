from api.models import Trip, Seat, TripReservation
from api.permissions import IsAirport
from api.serializers import TripSerializer, TripCreateSerializer
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
@permission_classes([IsAirport])
def create_trip(request):
    serializer = TripCreateSerializer(request.data)
    serializer.is_valid(raise_exception=True)
    pass


@extend_schema(
    responses=TripSerializer
)
@api_view(['GET'])
def get_trip(request, pk):
    obj = Trip.objects.get(pk=pk)
    serializer = TripSerializer(obj)
    return Response({'result': serializer.data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def book_seat(request, pk, seat_id):
    seat = Seat.objects.get(pk=seat_id)
    if seat.booked:
        return Response({'message': 'this seat is booked'}, status=status.HTTP_400_BAD_REQUEST)

    user = request.user
    trip = Trip.objects.get(pk=pk)
    obj = TripReservation.objects.create(trip=trip, seat=seat, user=user, cost=trip.get_offer_cost)
    obj.save()
    seat.booked = True
    seat.save()
    return Response({'message': 'seat booked'}, status=status.HTTP_201_CREATED)
