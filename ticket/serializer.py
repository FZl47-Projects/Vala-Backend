from .models import ticket ,ticketReply
from user.serializer import UserSerializer

from rest_framework import serializers

class TicketSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=ticket
        
        fields=['id','message','status','created','answerdTime','user']
      
class PostTicketSerializer(serializers.ModelSerializer):

    class Meta:
        model=ticket
        fields='__all__'
      
class TicketReplySerializer(serializers.ModelSerializer):

    class Meta:
        model=ticketReply
        
        fields='__all__'
      
class TicketReplyWithTicketSerializer(serializers.ModelSerializer):
    ticket=TicketSerializer()
    class Meta:
        model=ticketReply
        
        fields='__all__'
