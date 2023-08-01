from django.urls import path
from .views import ManagerDetail,ManagerList,ManagerUser
 
from rest_framework.generics import ListCreateAPIView

urlpatterns = [
path('all/',ManagerList.as_view()),   
path('GetId/<int:pk>/', ManagerDetail.as_view()),
path('GetId/', ManagerUser.as_view()),

]
