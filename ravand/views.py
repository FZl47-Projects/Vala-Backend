from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response



from django import http
from django.shortcuts import render

from .serializer import GetRavandSerializer,RavandSerializer,ImageRavandSerializer,PostImageRavandSerializer

from .models import ravand,imagesRavand
# Create your views here.

class RavandList(APIView):
    def get(self,request):
        querysert = ravand.objects.all()
        serial = GetRavandSerializer(querysert,many=True)
        return Response(serial.data)
    def post(self,request):
        serializer = RavandSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ImageRavandList(APIView):
    def get(self,request):
        querysert = imagesRavand.objects.all()
        serial = ImageRavandSerializer(querysert,many=True,context={'request': request})
        return Response(serial.data)
    def post(self,request):
        serializer = PostImageRavandSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class ImageRavandDetail(APIView):
    def get_object(self,pk):
        try:   
            return imagesRavand.objects.filter(ravand=pk)
        except imagesRavand.DoesNotExist:
            raise http.Http404
    def get(self,request,pk):
        queryset=self.get_object(pk)   
        serializer = ImageRavandSerializer(queryset,many=True,context={'request': request})
        return Response(serializer.data)

    def put(self,request,pk, format=None):
        queryset = self.get_object(pk)
        serializer = PostImageRavandSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class RavandDetail(APIView):
    def get_object(self,pk):
        try:   
            return ravand.objects.get(pk=pk)
        except ravand.DoesNotExist:
            raise http.Http404
    def get(self,request,pk):
        queryset=self.get_object(pk)   
        serializer = RavandSerializer(queryset)
        return Response(serializer.data)

    def put(self,request,pk, format=None):
        queryset = self.get_object(pk2)
        serializer = RavandSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class RavandUser(APIView):

    def get_object(self,user):
        try:   
            return ravand.objects.filter(user=user)
        except ravand.DoesNotExist:
            raise http.Http404
    def get(self,request):
        params = request.GET
        
        queryset=self.get_object(params['id'])   
        serializer = RavandSerializer(queryset,many=True)
        return Response(serializer.data)
