from api.models import AppUser
from api.serializers import UpdateBalanceSerializer, UserDetailsSerializer
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response


@extend_schema(
    request=UpdateBalanceSerializer
)
@api_view(['POST'])
@permission_classes([IsAdminUser])
def update_balance(request):
    serializer = UpdateBalanceSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = AppUser.objects.filter(email=serializer.data.get('email')).first()
    if user is None:
        return Response({'error': 'no such email'},status=status.HTTP_400_BAD_REQUEST)
    user.balance += serializer.data.get('balance')
    user.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_users(request):
    data = AppUser.objects.filter(is_airport=False).filter(is_staff=False).all()
    serializer = UserDetailsSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
