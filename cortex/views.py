# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.response import Response


# from django import http
# from django.shortcuts import render

# from .serializer import DistrictSerializer,CortexSerializer,GetCortexSerializer,Oprator_laserSerializer

# from .models import cortex,oprator_Laser,district
# # Create your views here.

# class CortexList(APIView):
#     def get(self,request):
#         querysert = cortex.objects.all()
#         serial = GetCortexSerializer(querysert,many=True)
#         return Response(serial.data)
#     def post(self,request):
#         serializer = CortexSerializer(data=request.data)
#         if serializer.is_valid():

#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class DistrictList(APIView):
#     def get(self,request):
#         querysert = district.objects.all()
#         serial = DistrictSerializer(querysert,many=True)
#         return Response(serial.data)
#     def post(self,request):
#         serializer = DistrictSerializer(data=request.data)
#         if serializer.is_valid():

#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CortexDetail(APIView):
#     def get_object(self,pk):
#         try:   
#             return cortex.objects.get(pk=pk)
#         except cortex.DoesNotExist:
#             raise http.Http404
#     def get_object_delete(self,pk):
#         try:   
#             return cortex.objects.filter(pk=pk)
#         except cortex.DoesNotExist:
#             raise http.Http404
#     def get(self,request,pk):
#         queryset=self.get_object(pk)   
#         serializer = GetCortexSerializer(queryset)
#         return Response(serializer.data)

#     def patch(self,request,pk, format=None):
#         queryset = self.get_object(pk)
#         serializer = CortexSerializer(queryset, data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object_delete(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# class CortexUser(APIView):

#     def get_object(self,user):
#         try:   
#             return cortex.objects.filter(user=user)
#         except cortex.DoesNotExist:
#             raise http.Http404
#     def get(self,request):
#         params = request.GET

#         queryset=self.get_object(params['id'])   
#         serializer = GetCortexSerializer(queryset,many=True)
#         return Response(serializer.data)


# class oprator_laserList(APIView):
#     def get(self,request):
#         querysert = oprator_Laser.objects.all()
#         serial = Oprator_laserSerializer(querysert,many=True)
#         return Response(serial.data)
#     def post(self,request):
#         serializer = Oprator_laserSerializer(data=request.data)
#         if serializer.is_valid():

#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class oprator_laserDetail(APIView):
#     def get_object(self,pk):
#         try:   
#             return oprator_Laser.objects.get(pk=pk)
#         except oprator_Laser.DoesNotExist:
#             raise http.Http404
#     def get_object_delete(self,pk):
#         try:   
#             return oprator_laser.objects.filter(pk=pk)
#         except oprator_laser.DoesNotExist:
#             raise http.Http404
#     def get(self,request,pk):
#         queryset=self.get_object(pk)   
#         serializer = Oprator_laserSerializer(queryset)
#         return Response(serializer.data)

#     def patch(self,request,pk, format=None):
#         queryset = self.get_object(pk)
#         serializer = Oprator_laserSerializer(queryset, data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object_delete(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# class oprator_laserUser(APIView):

#     def get_object(self,user):
#         try:   
#             return oprator_laser.objects.filter(user=user)
#         except oprator_laser.DoesNotExist:
#             raise http.Http404
#     def get(self,request):
#         params = request.GET

#         queryset=self.get_object(params['id'])   
#         serializer = Oprator_laserSerializer(queryset,many=True)
#         return Response(serializer.data)


# NEW
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from core import exceptions
from . import serializers, models


class District(APIView):
    permission_classes = ()  # TODO: should be complete | Add permission for admin

    def get(self, request):
        # get list objects
        districts = models.district.objects.all()
        # search
        search_q = request.GET.get('search',None)
        if search_q:
            districts = districts.filter(name__contains=search_q)
        return Response(serializers.DistrictSerializer(districts, many=True).data)

    def post(self, request):
        s = serializers.DistrictSerializer(data=request.data)
        try:
            s.is_valid(raise_exception=True)
        except Exception as e:
            raise exceptions.BadRequest
        district_name = s.validated_data['name']
        # check for unique district
        if models.district.objects.filter(name=district_name).exists():
            raise exceptions.Conflict
        obj = s.create(s.validated_data)
        return Response(serializers.DistrictSerializer(obj).data, status=status.HTTP_201_CREATED)


class DistrictDetail(APIView):
    permission_classes = ()  # TODO: should be complete | Add permission for admin

    def put(self,request,pk):
        # get object
        try:
            obj = models.district.objects.get(id=pk)
        except:
            raise exceptions.NotFound
        # check new values
        s = serializers.DistrictSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        # check for unique district
        if models.district.objects.filter(name=s.validated_data['name']).exists():
            raise exceptions.Conflict
        # update
        s.update(obj,s.validated_data)
        return Response(s.data)

    def delete(self, request, pk):
        try:
            obj = models.district.objects.get(id=pk)
        except:
            raise exceptions.NotFound({
                'district not found with this id'
            })
        obj.delete()
        return Response({
            'message': 'district deleted successfully !'
        })
