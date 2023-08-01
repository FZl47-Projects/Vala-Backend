from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response



from django import http
from django.shortcuts import render

from .serializer import FoodSerializer,ProgramGetSerializer,ProgramSerializer

from .models import food,program
# Create your views here.

class FoodList(APIView):
    def get(self,request):
        querysert = food.objects.all()
        serial = FoodSerializer(querysert,many=True,context={'request': request})
        return Response(serial.data)
    def post(self,request):
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FoodDetail(APIView):
    def get_object(self,pk):
        try:   
            return food.objects.get(pk=pk)
        except food.DoesNotExist:
            raise http.Http404
    def get(self,request,pk):
        queryset=self.get_object(pk)   
        serializer = FoodSerializer(queryset)
        return Response(serializer.data)

    def put(self,request,pk, format=None):
        queryset = self.get_object(pk)
        serializer = FoodSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProgramList(APIView):
    def get(self,request):
        querysert = program.objects.all()
        serial = ProgramGetSerializer(querysert,many=True,context={'request': request})
        return Response(serial.data)
    def post(self,request):
        serializer = ProgramSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProgramDetail(APIView):
    def get_object(self,pk):
        try:   
            return program.objects.get(pk=pk)
        except program.DoesNotExist:
            raise http.Http404
    def get(self,request,pk):
        queryset=self.get_object(pk)   
        serializer = ProgramGetSerializer(queryset)
        return Response(serializer.data)

    def put(self,request,pk, format=None):
        queryset = self.get_object(pk)
        serializer = ProgramSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ProgramUser(APIView):

    def get_object(self,user):
        try:   
            return program.objects.filter(user=user)
        except program.DoesNotExist:
            raise http.Http404
    def get(self,request):
        params = request.GET
        
        queryset=self.get_object(params['id'])   
        serializer = ProgramGetSerializer(queryset,many=True,context={'request': request})
        return Response(serializer.data)
