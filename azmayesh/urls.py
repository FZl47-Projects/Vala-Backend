from django.urls import path
from .views import AzmayeshDetail,AzmayeshList,AzmayeshUser
 
from rest_framework.generics import ListCreateAPIView

urlpatterns = [
path('all/',AzmayeshList.as_view()),   
path('GetId/<int:pk>/', AzmayeshDetail.as_view()),
path('GetId/', AzmayeshUser.as_view()),

]
