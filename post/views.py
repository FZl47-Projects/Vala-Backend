from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response



from django import http
from django.shortcuts import render

from .serializer import PostSerializer,CategorySerializer,InsertPostSerializer

from .models import post,category
# Create your views here.

class PostList(APIView):
    def get(self,request):
        querysert = post.objects.all()
        serial = PostSerializer(querysert,many=True,context={'request': request})
        return Response(serial.data)
    def post(self,request):
        serializer = InsertPostSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryList(APIView):
    def get(self,request):
        querysert = category.objects.all()
        serial = CategorySerializer(querysert,many=True,context={'request': request})
        return Response(serial.data)
    def post(self,request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostDetail(APIView):
    def get_object(self,pk):
        try:   
            return post.objects.get(pk=pk)
        except post.DoesNotExist:
            raise http.Http404
    def get(self,request,pk):
        queryset=self.get_object(pk)   
        serializer = PostSerializer(queryset)
        return Response(serializer.data)

    def put(self,request,pk, format=None):
        queryset = self.get_object(pk)
        serializer = InsertPostSerializer(queryset,partial=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryDetail(APIView):
    def get_object(self,pk):
        try:   
            return category.objects.get(pk=pk)
        except category.DoesNotExist:
            raise http.Http404
    def get(self,request,pk):
        queryset=self.get_object(pk)   
        serializer = CategorySerializer(queryset)
        return Response(serializer.data)

    def patch(self,request,pk, format=None):
        queryset = self.get_object(pk)
        serializer = CategorySerializer(queryset, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class PostUser(APIView):
    def get_object(self,user):
        try:   
            return post.objects.filter(oprator=user)
        except post.DoesNotExist:
            raise http.Http404
    def get(self,request):
        params = request.GET
        queryset=self.get_object(params['id'])   
        serializer = PostSerializer(queryset,many=True,context={'request': request})
        return Response(serializer.data)
