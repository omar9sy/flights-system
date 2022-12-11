from api.models import Trip
from api.serializers import TripSerializer
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@extend_schema(
    responses=TripSerializer
)
@api_view(['GET'])
def get_trips(request):
    query = Trip.objects.all()
    serializer = TripSerializer(query, many=True)
    result = {'result': serializer.data}
    return Response(result, status=status.HTTP_200_OK)
