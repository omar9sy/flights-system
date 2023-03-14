import decimal
from api.models import Trip, Seat, TripReservation, Airport, AppUser, Restaurant, Hotel
from api.permissions import IsAirport, IsAirportOrReadOnly
from api.serializers import TripSerializer, TripCreateSerializer, TripReservationSerializer, RestaurantSerializer, \
    HotelSerializer, ResultSerializer
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import mixins, views
from rest_framework.viewsets import GenericViewSet

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
    for _ in range(10):
        obj = Seat.objects.create(trip=trip, level=1, cost=costs[0])
        obj.save()

    for _ in range(20):
        obj = Seat.objects.create(trip=trip, level=2, cost=costs[1])
        obj.save()

    for _ in range(30):
        obj = Seat.objects.create(trip=trip, level=2, cost=costs[2])
        obj.save()

    result = TripSerializer(trip)
    return Response({'result': result.data}, status=status.HTTP_201_CREATED)


class TripViewSet(mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               GenericViewSet):
    authentication_classes = [IsAuthenticated, IsAirportOrReadOnly]
    serializer_class = TripSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'result': serializer.data})
    
@extend_schema(
    responses=TripReservationSerializer
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


@extend_schema(
    parameters=[
        OpenApiParameter(name='day', description='day of month to search in', required=False, type=int),
        OpenApiParameter(name='month', description='month to search in', required=False, type=int),
        OpenApiParameter(name='destination_city', description='destination_city to get trips for', required=False, type=str),
        OpenApiParameter(name='departure_city', description='departure_city to get trips for', required=False, type=str),
    ],
    responses={
        200: TripSerializer,
    }
)
@api_view(['GET'])
def search_trip(request):
    day = request.query_params.get('day')
    month = request.query_params.get('month')
    destination_city = request.query_params.get('destination_city')
    departure_city = request.query_params.get('departure_city')
    
    data = Trip.objects.all()
    if month is not None:
        data = data.filter(departure_date__month=month)
    
    if day is not None:
        data = data.filter(departure_date__day=day)
    
    if destination_city is not None:
        data = data.filter(destination_city=destination_city)
    
    if departure_city is not None:
        data = data.filter(airport__city=departure_city)

    serializer = TripSerializer(data, many=True)

    return Response({'result': serializer.data})
