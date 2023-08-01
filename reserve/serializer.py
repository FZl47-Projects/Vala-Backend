from rest_framework import serializers
from .models import reserve,service 
from user.serializer import UserSerializer
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=service
        fields='__all__'
class ReserveSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model=reserve
        fields='__all__'
class PostReserveSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=reserve
        fields='__all__'

