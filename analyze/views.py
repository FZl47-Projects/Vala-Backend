from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response



from django import http
from django.shortcuts import render

from .serializer import AnalyzeSerializer,PostAnalyzeSerializer
from .models import analyze
# Create your views here.

class AnalyzeList(APIView):
    def get(self,request):
        querysert = analyze.objects.all()
        serial = AnalyzeSerializer(querysert,many=True,context={'request': request})
        return Response(serial.data)
    def post(self,request):
        serializer = PostAnalyzeSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AnalyzeDetail(APIView):
    def get_object(self,pk):
        try:   
            return analyze.objects.get(pk=pk)
        except analyze.DoesNotExist:
            raise http.Http404
    def get_object_delete(self,pk):
        try:   
            return analyze.objects.filter(pk=pk)
        except analyze.DoesNotExist:
            raise http.Http404
    def get(self,request,pk):
        queryset=self.get_object(pk)   
        serializer = AnalyzeSerializer(queryset,context={'request': request})
        return Response(serializer.data)

    def patch(self,request,pk, format=None):
        queryset = self.get_object(pk)
        serializer = PostAnalyzeSerializer(queryset, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object_delete(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class AnalyzeUser(APIView):

    def get_object(self,user):
        try:   
            return analyze.objects.filter(user=user)
        except analyze.DoesNotExist:
            raise http.Http404
    def get(self,request):
        params = request.GET
        
        queryset=self.get_object(params['id'])   
        serializer = AnalyzeSerializer(queryset,many=True,context={'request': request})
        return Response(serializer.data)
