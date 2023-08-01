from .models import story ,category
from rest_framework import serializers
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=category
        fields='__all__'
class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model=story
        fields='__all__'