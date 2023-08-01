from .models import routin 
from rest_framework import serializers
class RoutinSerializer(serializers.ModelSerializer):
    class Meta:
        model=routin
        fields='__all__'