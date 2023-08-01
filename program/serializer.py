from rest_framework import serializers
from user.serializer import UserSerializer
from manager.serializer import ManagerSerializer
from .models import food,program


class ProgramSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=program
        fields='__all__'
class ProgramGetSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    oprator=ManagerSerializer()
    class Meta:
        model=program
        fields=['user','created','oprator','types','diet']
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model=food
        fields='__all__'


