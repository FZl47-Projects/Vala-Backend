from .models import analyze 
from user.serializer import UserSerializer
from rest_framework import serializers
class AnalyzeSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=analyze
        fields=['image1','image2','image3','user']
class PostAnalyzeSerializer(serializers.ModelSerializer):
    class Meta:
        model=analyze
        fields='__all__'