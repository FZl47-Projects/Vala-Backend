from .models import comment,commentService
from rest_framework import serializers
from user.serializer import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=comment
        fields='__all__'
class CommentServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=commentService
        fields='__all__'
class GetCommentSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=comment
        fields=['pk' ,'post','text','user' , 'accepted' ]
