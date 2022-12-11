from api.models import Airport
from api.serializers import AirportSerializer
from rest_framework import viewsets


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

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
