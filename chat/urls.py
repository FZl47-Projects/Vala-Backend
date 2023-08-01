from django.urls import path
from .views import ChatDetail,ChatList,ChatUser
 
from rest_framework.generics import ListCreateAPIView

urlpatterns = [
path('all/',ChatList.as_view()),   
path('GetId/<int:pk>/', ChatDetail.as_view()),
path('GetId/', ChatUser.as_view()),


]
