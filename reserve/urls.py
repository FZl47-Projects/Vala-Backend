from django.urls import path
from .views import ServiceDetail,ServiceList,ReserveDetail,ReserveList,ReserveUser
 
from rest_framework.generics import ListCreateAPIView

urlpatterns = [
path('all/',ServiceList.as_view()),   
path('GetId/<int:pk>/', ServiceDetail.as_view()),



path('reserve/all/',ReserveList.as_view()),   
path('reserve/GetId/<int:pk>/', ReserveDetail.as_view()),
path('reserve/GetId/', ReserveUser.as_view()),
]
