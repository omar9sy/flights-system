from api.models import Airport, AppUser, Trip
from api.models import AllowedEmailForAirport
from api.permissions import IsAirport, IsAirportOrReadOnly
from api.serializers import AirportSerializer, AirporCreatetSerializer,AllowedEmailForAirportSerializer, TripSerializer
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from rest_framework import generics, mixins, views
from rest_framework.viewsets import GenericViewSet

class AirportViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Airport.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAirportOrReadOnly]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return AirporCreatetSerializer
        return AirportSerializer

    def list(self, request, *args, **kwargs):
        data = self.queryset
        serializer = self.get_serializer(data, many=True)
        return Response({'result': serializer.data})

    def retrieve(self, request, *args, **kwargs):
        data = get_object_or_404(self.queryset, pk=kwargs.get('pk'))
        serializer = self.get_serializer(data)
        return Response({'result': serializer.data})

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@extend_schema(
    request=AllowedEmailForAirportSerializer,
    responses=AllowedEmailForAirportSerializer
)
@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_email(request):
    email = request.data.get('Email')
    
    if AllowedEmailForAirport.objects.all().filter(Email=email).count() != 0:
        return Response({'error': 'email not allowed1'}, status=status.HTTP_400_BAD_REQUEST)
    
    if AppUser.objects.all().filter(email=email).count() != 0:
        return Response({'error': 'email not allowed2'}, status=status.HTTP_400_BAD_REQUEST)
    
    obj = AllowedEmailForAirportSerializer(data=request.data)
    obj.is_valid(raise_exception=True)
    obj.save()

    return Response(obj.data, status=status.HTTP_201_CREATED)


@extend_schema(
    responses=TripSerializer
)
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAirport])
def get_airport_trips(request):
    user = request.user
    airport = Airport.objects.filter(author=user).first()
    data = Trip.objects.filter(airport=airport)
    serializer = TripSerializer(data,many=True)
    return Response({'result': serializer.data})
