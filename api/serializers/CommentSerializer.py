from api.models import Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Comment
        fields = ['text', 'created_at', 'author', 'id']


class CommentCreateSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Comment
        fields = ['text']
