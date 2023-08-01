from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response



from django import http
from django.shortcuts import render

from .serializer import ChatSerializer,GetchatSerializer

from .models import chat
# Create your views here.

class ChatList(APIView):
    def get(self,request):
        querysert = chat.objects.all()
        serial = GetchatSerializer(querysert,many=True,context={'request': request})
        return Response(serial.data)
    def post(self,request):
        serializer = ChatSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ChatDetail(APIView):
    def get_object(self,pk):
        try:   
            return chat.objects.get(pk=pk)
        except chat.DoesNotExist:
            raise http.Http404
    def get(self,request,pk):
        queryset=self.get_object(pk)   
        serializer = GetchatSerializer(queryset)
        return Response(serializer.data)

    def put(self,request,pk, format=None):
        queryset = self.get_object(pk)
        serializer = ChatSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ChatUser(APIView):

    def get_object(self,user):
        try:   
            return chat.objects.filter(user=user)
        except chat.DoesNotExist:
            raise http.Http404
    def get(self,request):
        params = request.GET
        
        queryset=self.get_object(params['id'])   
        serializer = GetchatSerializer(queryset,many=True)
        return Response(serializer.data)
    