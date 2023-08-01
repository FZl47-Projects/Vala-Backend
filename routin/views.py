from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response



from django import http
from django.shortcuts import render

from .serializer import RoutinSerializer

from .models import routin
# Create your views here.

class RoutinList(APIView):
    def get(self,request):
        querysert = routin.objects.all()
        serial = RoutinSerializer(querysert,many=True)
        return Response(serial.data)
    def post(self,request):
        serializer = RoutinSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class RoutinDetail(APIView):
    def get_object(self,pk):
        try:   
            return routin.objects.get(pk=pk)
        except routin.DoesNotExist:
            raise http.Http404
    def get(self,request,pk):
        queryset=self.get_object(pk)   
        serializer = RoutinSerializer(queryset)
        return Response(serializer.data)

    def put(self,request,pk, format=None):
        queryset = self.get_object(pk)
        serializer = RoutinSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class RoutinUser(APIView):

    def get_object(self,user):
        try:   
            return routin.objects.filter(user=user)
        except routin.DoesNotExist:
            raise http.Http404
    def get(self,request):
        params = request.GET
        
        queryset=self.get_object(params['id'])   
        serializer = RoutinSerializer(queryset,many=True)
        return Response(serializer.data)