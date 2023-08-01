from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response



from django import http
from django.shortcuts import render

from .serializer import AzmayeshSerializer
from .models import azmayesh
# Create your views here.

class AzmayeshList(APIView):
    def get(self,request):
        querysert = azmayesh.objects.all()
        serial = AzmayeshSerializer(querysert,many=True)
        return Response(serial.data)
    def post(self,request):
        serializer = AzmayeshSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AzmayeshDetail(APIView):
    def get_object(self,pk):
        try:   
            return azmayesh.objects.get(pk=pk)
        except azmayesh.DoesNotExist:
            raise http.Http404
    def get_object_delete(self,pk):
        try:   
            return azmayesh.objects.filter(pk=pk)
        except azmayesh.DoesNotExist:
            raise http.Http404
    def get(self,request,pk):
        queryset=self.get_object(pk)   
        serializer = AzmayeshSerializer(queryset)
        return Response(serializer.data)

    def put(self,request,pk, format=None):
        queryset = self.get_object(pk)
        serializer = AzmayeshSerializer(queryset, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object_delete(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class AzmayeshUser(APIView):

    def get_object(self,user):
        try:   
            return azmayesh.objects.filter(user=user)
        except azmayesh.DoesNotExist:
            raise http.Http404
    def get(self,request):
        params = request.GET
        
        queryset=self.get_object(params['id'])   
        serializer = AzmayeshSerializer(queryset,many=True)
        return Response(serializer.data)
