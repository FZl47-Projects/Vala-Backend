from .models import product,order
from rest_framework import serializers
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields='__all__'
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=order
        fields='__all__'