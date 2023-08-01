from django.contrib.auth import authenticate
from django.db.models import Q
from django import http
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from core import exceptions
from .serializer import UserSerializer, LoginSerializer, UserBasicSerializer, TokenSerializer, UserLoginSerializer
from .models import user


class UserList(APIView):
    def get(self, request):
        querysert = user.objects.all()
        serial = UserSerializer(querysert, many=True, context={'request': request})
        return Response(serial.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return user.objects.get(pk=pk)
        except user.DoesNotExist:
            raise http.Http404

    def get_object_delete(self, pk):
        try:
            return user.objects.filter(pk=pk)
        except user.DoesNotExist:
            raise http.Http404

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = UserSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = UserSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object_delete(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserUser(APIView):

    def get_object(self, user):
        try:
            return user.objects.filter(user=user)
        except user.DoesNotExist:
            raise http.Http404

    def get(self, request):
        params = request.GET

        queryset = self.get_object(params['id'])
        serializer = UserSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


class UserLogin(APIView):

    def get_object(self, phone_number, password):
        try:
            print('+98' + phone_number)
            return user.objects.filter(phone_number='+98' + phone_number, password=password)
        except user.DoesNotExist:
            raise http.Http404

    def get(self, request):
        params = request.GET

        queryset = self.get_object(params['phone'], params['password'])
        serializer = LoginSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)


# NEW

class UserAuthLogin(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        s = UserLoginSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        username = s.validated_data['username']
        password = s.validated_data['password']
        user = authenticate(request, username=username, password=password)
        if not user:
            raise exceptions.NotFound({
                'detail': 'user not found with this username and password'
            })
        try:
            # delete old token
            token = Token.objects.get(user=user)
            token.delete()
        except:
            pass
        token = Token.objects.create(user=user)
        return Response(TokenSerializer(token).data)


class User(APIView):

    def get(self, request):
        data = request.GET
        search = data.get('search', None)
        user_model = user
        users = user_model.objects.filter(is_staff=False)  # get normal users(not admins)
        if search:
            lookup = Q(first_name__contains=search) | Q(last_name__contains=search) | Q(email__icontains=search)
            users = users.filter(lookup)
        return Response(UserBasicSerializer(users, many=True).data)
