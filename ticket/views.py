from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response



from django import http
from django.shortcuts import render

from .serializer import TicketSerializer,PostTicketSerializer,TicketReplySerializer,TicketReplyWithTicketSerializer
from .models import ticket,ticketReply
# Create your views here.


class TicketList(APIView):
    def get(self,request):
        querysert = ticket.objects.all()
        serial = TicketSerializer(querysert,many=True)
        return Response(serial.data)
    def post(self,request):
        serializer = PostTicketSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TicketDetail(APIView):
    def get_object(self,pk):
        try:   
            return ticket.objects.get(pk=pk)
        except ticket.DoesNotExist:
            raise http.Http404
    def get(self,request,pk):
        queryset=self.get_object(pk)   
        serializer = TicketSerializer(queryset)
        return Response(serializer.data)

    def patch(self,request,pk, format=None):
        queryset = self.get_object(pk)
        serializer = PostTicketSerializer(queryset, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class TicketUser(APIView):
    def get_object(self,user):
        try:   
            return ticket.objects.filter(user=user)
        except ticket.DoesNotExist:
            raise http.Http404
    def get(self,request):
        params = request.GET
        
        queryset=self.get_object(params['id'])   
        serializer = TicketSerializer(queryset,many=True)
        return Response(serializer.data)

class TicketReplyList(APIView):
    def get(self,request):
        querysert = ticketReply.objects.all()
        serial = TicketReplySerializer(querysert,many=True)
        return Response(serial.data)
    def post(self,request):
        serializer = TicketReplySerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TicketReplyDetail(APIView):
    def get_object(self,pk):
        try:   
            return ticketReply.objects.get(pk=pk)
        except ticketReply.DoesNotExist:
            raise http.Http404
    def get(self,request,pk):
        queryset=self.get_object(pk)   
        serializer = TicketReplySerializer(queryset)
        return Response(serializer.data)

    def put(self,request,pk, format=None):
        queryset = self.get_object(pk)
        serializer = TicketReplySerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TicketreplyeUser(APIView):
    def get_object(self,user):
        try:   
            return ticketReply.objects.filter(oprator=user)
        except ticketReply.DoesNotExist:
            raise http.Http404
    def get(self,request):
        params = request.GET
        
        queryset=self.get_object(params['id'])   
        serializer = TicketReplyWithTicketSerializer(queryset,many=True)
        return Response(serializer.data)
