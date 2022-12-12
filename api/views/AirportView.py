from api.models import Airport
from api.permissions import IsAirport
from api.serializers import AirportSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAirport]

    def list(self, request, *args, **kwargs):
        data = self.queryset
        serializer = self.serializer_class(data,many=True)
        return Response({'result': serializer.data})

    def retrieve(self, request, *args, **kwargs):
        data = get_object_or_404(self.queryset, pk=kwargs.get('pk'))
        serializer = self.serializer_class(data)
        return Response({'result': serializer.data})

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

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
