from api.models import Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['text', 'created_at', 'author', 'id']
        read_only_fields = ['created_at', 'author', 'id']
