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
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from core import exceptions
from . import serializers, models


class District(APIView):

    def get(self, request):
        import time
        time.sleep(1)

        # get list objects
        districts = models.district.objects.all()
        # search
        search_q = request.GET.get('search', None)
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

    def put(self, request, pk):
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
        s.update(obj, s.validated_data)
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


class CortextUser(APIView):

    # TEST
    def create_user(self):
        return models.user.objects.get_or_create(defaults={'name': 'Fazel Momeni'},
                                                 name='Fazel Momeni',
                                                 phone_number='09130009999',
                                                 age=19,
                                                 weight=55,
                                                 height=180,
                                                 nationalcode=3300330033,
                                                 password='its_joke',
                                                 birthday='2020-01-1',
                                                 wallet=0
                                                 )

    def get(self, request, user_id):
        # TEST
        user_id = models.user.objects.first().id


        if not user_id:
            raise exceptions.BadRequest({
                'detail': 'user-id param is not valid'
            })
        try:
            user_obj = models.user.objects.get(id=user_id)
        except models.user.DoesNotExist:
            raise exceptions.NotFound
        cortexes = user_obj.cortex_set.all()
        cortexes_data = serializers.CortexSerializer(cortexes, many=True).data
        user_data = serializers.CortextUserSerializer(user_obj).data
        context = {
            'cortexes': cortexes_data,
            'user': user_data
        }
        return Response(context)


class Operator(APIView):

    # TEST
    def create_operator(self):
        return models.oprator_Laser.objects.create(
            name='Dr Fereshte Ghasemi',
            phonenumber='09103011010'
        )

    def get(self, request):
        operators = models.oprator_Laser.objects.all()
        return Response(serializers.OperatorLaserSerializer(operators, many=True).data)


class Cortex(APIView):

    def post(self, request):
        data = request.data
        if not data:
            raise exceptions.BadRequest
        is_new = data.get('is_new',True)
        if not is_new:
            raise exceptions.Conflict
        districts = data.get('cortexes', None)
        if isinstance(districts, list) is False:
            raise exceptions.BadRequest

        operator_id = data.get('operator', 0)
        user_id = data.get('user_id',0)
        try:
            cortex = models.cortex.objects.create(user_id=user_id,oprator_Las_id=operator_id)
        except:
            raise exceptions.BadRequest({
                'detail':'enter user_id and operator_id correctly'
            })

        for district in districts:
            models.cortex_district.objects.create(
                cortex=cortex,
                district_id=district['id'],
                intensity_value=district['intensity_value']
            )

        return Response(serializers.CortexSerializer(cortex).data)


class CortexDetail(APIView):

    def delete(self, request, cortex_id):
        try:
            obj = models.cortex.objects.get(id=cortex_id)
            obj.delete()
        except:
            raise exceptions.NotFound
        return Response({
            'message': 'cortex object deleted successfully!'
        })


class CortexDistrictDetail(APIView):

    def delete(self, request, cortex_id, district_id):
        try:
            obj = models.cortex_district.objects.get(cortex_id=cortex_id, district_id=district_id)
            obj.delete()
        except:
            raise exceptions.NotFound
        return Response({
            'message': 'cortex district object deleted successfully!'
        })
