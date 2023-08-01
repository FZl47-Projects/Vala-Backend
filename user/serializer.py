from .models import user
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['id']


# NEW

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(
        style={'input_type': 'password'}
    )


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key',)


class UserBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('id', 'first_name', 'last_name', 'email')
