from .models import ravand ,imagesRavand
from user.serializer import UserSerializer
from rest_framework import serializers
class RavandSerializer(serializers.ModelSerializer):
    class Meta:
        model=ravand
        fields='__all__'

class GetRavandSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model=ravand
        fields='__all__'
class ImageRavandSerializer(serializers.ModelSerializer):
    class Meta:
        model=imagesRavand
        fields='__all__'
class PostImageRavandSerializer(serializers.ModelSerializer):
    RavandSerializer()
    class Meta:
        model=imagesRavand
        fields='__all__'
