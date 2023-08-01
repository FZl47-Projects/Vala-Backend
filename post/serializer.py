from .models import post ,category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=category
        fields='__all__'
class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model=post
        fields=['id','file','poster','title','description','like','created','isDelete','types','oprator','category']

class InsertPostSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=post
        fields='__all__'
