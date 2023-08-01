from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response



from django import http
from django.shortcuts import render

from .serializer import ProductSerializer,OrderSerializer

from .models import product,order
# Create your views here.

class ProductList(APIView):
    def get(self,request):
        querysert = product.objects.all()
        serial = ProductSerializer(querysert,many=True ,context={'request': request})
        return Response(serial.data)
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetail(APIView):
    def get_object(self,pk):
        try:   
            return product.objects.get(pk=pk)
        except product.DoesNotExist:
            raise http.Http404
    def get(self,request,pk):
        queryset=self.get_object(pk)   
        serializer = ProductSerializer(queryset,context={'request': request})
        return Response(serializer.data)

    def put(self,request,pk, format=None):
        queryset = self.get_object(pk)
        serializer = ProductSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    

class OrderList(APIView):
    def get(self,request):
        querysert = order.objects.all()
        serial = OrderSerializer(querysert,many=True)
        return Response(serial.data)
    def post(self,request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class OrderDetail(APIView):
    def get_object(self,pk):
        try:   
            return order.objects.get(pk=pk)
        except order.DoesNotExist:
            raise http.Http404
    def get(self,request,pk):
        queryset=self.get_object(pk)   
        serializer = OrderSerializer(queryset)
        return Response(serializer.data)

    def put(self,request,pk, format=None):
        queryset = self.get_object(pk)
        serializer = OrderSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class OrderUser(APIView):

    def get_object(self,user):
        try:   
            return order.objects.filter(user=user)
        except order.DoesNotExist:
            raise http.Http404
    def get(self,request):
        params = request.GET
        
        queryset=self.get_object(params['id'])   
        serializer = OrderSerializer(queryset,many=True)
        return Response(serializer.data)