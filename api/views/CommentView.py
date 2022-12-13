from api.models import Comment
from api.serializers import CommentSerializer, CommentCreateSerializer
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


@permission_classes([IsAuthenticatedOrReadOnly])
@extend_schema(
    responses=CommentSerializer,
    request=CommentCreateSerializer
)
@api_view(['GET', 'POST'])
def get_comments(request):
    if request.method == 'GET':
        data = Comment.objects.all()
        serializer = CommentSerializer(data, many=True)
        return Response({'result': serializer.data})
    else:
        serializer = CommentCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        return Response({'result': serializer.data}, status=status.HTTP_201_CREATED)
