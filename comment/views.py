from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response



from django import http
from django.shortcuts import render

from .serializer import CommentSerializer,GetCommentSerializer,CommentServiceSerializer

from .models import comment,commentService
# Create your views here.

class CommentList(APIView):
    def get(self,request):
        querysert = comment.objects.all()
        serial = GetCommentSerializer(querysert,many=True)
        return Response(serial.data)
    def post(self,request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CommentDetail(APIView):
    def get_object(self,pk):
        try:   
            return comment.objects.get(pk=pk)
        except comment.DoesNotExist:
            raise http.Http404
    def get_object_delete(self,pk):
        try:   
            return comment.objects.filter(pk=pk)
        except comment.DoesNotExist:
            raise http.Http404
    def get(self,request,pk):
        queryset=self.get_object(pk)   
        serializer = GetCommentSerializer(queryset)
        return Response(serializer.data)

    def put(self,request,pk, format=None):
        queryset = self.get_object(pk)
        serializer = CommentSerializer(queryset, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object_delete(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class CommentUser(APIView):

    def get_object(self,user):
        try:   
            return comment.objects.filter(post=user)
        except comment.DoesNotExist:
            raise http.Http404
    def get(self,request):
        params = request.GET
        
        queryset=self.get_object(params['id'])   
        serializer = GetCommentSerializer(queryset,many=True)
        return Response(serializer.data)



class CommentServiceList(APIView):
    def get(self,request):
        querysert = commentService.objects.all()
        serial = CommentServiceSerializer(querysert,many=True)
        return Response(serial.data)
    def post(self,request):
        serializer = CommentServiceSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CommentServiceDetail(APIView):
    def get_object(self,pk):
        try:   
            return commentService.objects.get(pk=pk)
        except commentService.DoesNotExist:
            raise http.Http404
    def get_object_delete(self,pk):
        try:   
            return commentService.objects.filter(pk=pk)
        except commentService.DoesNotExist:
            raise http.Http404
    def get(self,request,pk):
        queryset=self.get_object(pk)   
        serializer = CommentServiceSerializer(queryset)
        return Response(serializer.data)

    def patch(self,request,pk, format=None):
        queryset = self.get_object(pk)
        serializer = CommentServiceSerializer(queryset, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        snippet = self.get_object_delete(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class CommentServiceUser(APIView):

    def get_object(self,user):
        try:   
            return commentService.objects.filter(manager=user)
        except commentService.DoesNotExist:
            raise http.Http404
    def get(self,request):
        params = request.GET
        
        queryset=self.get_object(params['id'])   
        serializer = CommentServiceSerializer(queryset,many=True)
        return Response(serializer.data)
