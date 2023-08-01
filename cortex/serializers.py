# from .models import  district,cortex,oprator_Laser 
# from rest_framework import serializers
# from user.serializer import UserSerializer
# class CortexSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=cortex
#         fields='__all__'
# class GetCortexSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#     class Meta:
#         model=cortex
#         fields=['district','numbermeet','descriptions','oprator_Las','created','user']
# class Oprator_laserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=oprator_Laser
#         fields='__all__'
# class DistrictSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=district
#         fields='__all__'


# NEW
from rest_framework import serializers
from . import models

class DistrictSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.district
        # fields = ('id','name')
        fields = '__all__'

        