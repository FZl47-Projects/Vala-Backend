from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response



from django import http
from django.shortcuts import render

from .serializer import ManagerSerializer

from .models import manager
# Create your views here.

class ManagerList(APIView):
    def get(self,request):
        querysert = manager.objects.all()
        serial = ManagerSerializer(querysert,many=True)
        return Response(serial.data)
    def post(self,request):
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ManagerDetail(APIView):
    def get_object(self,pk):
        try:   
            return manager.objects.get(pk=pk)
        except manager.DoesNotExist:
            raise http.Http404
    def get_object_delete(self,pk):
        try:   
            return manager.objects.filter(pk=pk)
        except manager.DoesNotExist:
            raise http.Http404
    def get(self,request,pk):
        queryset=self.get_object(pk)   
        serializer = ManagerSerializer(queryset)
        return Response(serializer.data)

    def put(self,request,pk, format=None):
        queryset = self.get_object(pk)
        serializer = ManagerSerializer(queryset, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object_delete(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class ManagerUser(APIView):

    def get_object(self,user):
        try:   
            return manager.objects.filter(user=user)
        except manager.DoesNotExist:
            raise http.Http404
    def get(self,request):
        params = request.GET
        
        queryset=self.get_object(params['id'])   
        serializer = ManagerSerializer(queryset,many=True)
        return Response(serializer.data)
