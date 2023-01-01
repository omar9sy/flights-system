from api.models import Airport, AppUser
from api.models import AllowedEmailForAirport
from api.permissions import IsAirport
from api.serializers import AirportSerializer, AirporCreatetSerializer, AllowedEmailForAirportSerializer
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, IsAirport]

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
    if AllowedEmailForAirport.objects.filter(Email=email).count() != 0:
        return Response({'error': 'email not allowed'}, status=status.HTTP_400_BAD_REQUEST)
    if AppUser.objects().filter(email=email).count != 0:
        return Response({'error': 'email not allowed'}, status=status.HTTP_400_BAD_REQUEST)
    obj = AllowedEmailForAirportSerializer(data=request.data)
    obj.is_valid(raise_exception=True)
    obj.save()
    return Response(obj.data, status=status.HTTP_201_CREATED)

# @extend_schema(
#     responses=AirportSerializer
# )
# @api_view(['GET'])
# def get_airports(request):
#     query = Airport.objects.all()
#     serializer = AirportSerializer(query, many=True)
#     result = {'result': serializer.data}
#     return Response(result, status=status.HTTP_200_OK)


# @extend_schema(
#     responses=AirportSerializer
# )
# @api_view(['GET'])
# def get_airport(request, pk):
#     query = Airport.objects.get(pk=pk)
#     serializer = AirportSerializer(query)
#     result = {'result': serializer.data}
#     return Response(result, status=status.HTTP_200_OK)
