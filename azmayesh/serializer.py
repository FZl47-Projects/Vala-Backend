from .models import azmayesh 
from rest_framework import serializers
class AzmayeshSerializer(serializers.ModelSerializer):
    class Meta:
        model=azmayesh
        fields='__all__'