from django.urls import path
from .views import RoutinDetail,RoutinList,RoutinUser
 
from rest_framework.generics import ListCreateAPIView

urlpatterns = [
path('all/',RoutinList.as_view()),   
path('GetId/<int:pk>/', RoutinDetail.as_view()),
path('GetId/', RoutinUser.as_view()),

]
