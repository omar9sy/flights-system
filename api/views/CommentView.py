from api.models import Comment, AppUser
from api.serializers import CommentSerializer
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


@extend_schema(
    responses=CommentSerializer,
    request=CommentSerializer
)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_comments(request):
    if request.method == 'GET':
        data = Comment.objects.all()
        serializer = CommentSerializer(data, many=True)
        return Response({'result': serializer.data})
    else:
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        author = AppUser.objects.get(pk=request.user.id)
        serializer.save(author=author)

        return Response({'result': serializer.data}, status=status.HTTP_201_CREATED)
