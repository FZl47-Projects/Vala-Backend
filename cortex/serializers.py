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
        fields = '__all__'
        extra_kwargs = {'name': {
            'required': True
        }
        }

class OperatorLaserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.oprator_Laser
        fields = ('id', 'name', 'phonenumber')


class CortextUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.user
        fields = ('name','nationalcode','phone_number')


class CortexDistrictSerializer(serializers.ModelSerializer):
    district = serializers.CharField(read_only=True, source='district.name')

    class Meta:
        model = models.cortex_district
        exclude = ('cortext',)


class CortexSerializer(serializers.ModelSerializer):
    districts = CortexDistrictSerializer(source='cortex_district__set', many=True)
    operator = OperatorLaserSerializer(source='oprator_Laser')

    class Meta:
        model = models.cortex
        exclude = ('oprator_Laser',)



