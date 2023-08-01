from .models import manager 
from rest_framework import serializers
class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model=manager
        fields='__all__'