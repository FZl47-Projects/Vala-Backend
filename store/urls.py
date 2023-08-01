
from django.urls import path
from .views import OrderDetail,ProductDetail,OrderList,ProductList,OrderUser
 
from rest_framework.generics import ListCreateAPIView

urlpatterns = [
path('all/',OrderList.as_view()),   
path('GetId/<int:pk>/', OrderDetail.as_view()),
path('GetId/',OrderUser.as_view()),

path('product/all/',ProductList.as_view()),   
path('product/GetId/<int:pk>/', ProductDetail.as_view()),

]
