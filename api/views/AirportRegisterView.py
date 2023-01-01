from api.models import AllowedEmailForAirport
from api.serializers import AirportRegisterSerializer
from dj_rest_auth.registration.views import RegisterView
from rest_framework import status
from rest_framework.response import Response


class AirportRegisterView(RegisterView):
    serializer_class = AirportRegisterSerializer

    def post(self, request, *args, **kwargs):
        email = self.request.data.get('email')
        if AllowedEmailForAirport.objects.filter(Email=email).count() == 0:
            return Response({'error': 'email not allowed'}, status=status.HTTP_400_BAD_REQUEST)
        return self.create(request, *args, **kwargs)
