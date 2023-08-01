from django.urls import path
from .views import CommentDetail,CommentServiceDetail,CommentList,CommentServiceList,CommentUser,CommentServiceUser

from rest_framework.generics import ListCreateAPIView

urlpatterns = [
path('all/',CommentList.as_view()),   
path('GetId/<int:pk>/', CommentDetail.as_view()),
path('GetId/', CommentUser.as_view()),
path('service/all/',CommentServiceList.as_view()),   
path('service/GetId/<int:pk>/', CommentServiceDetail.as_view()),
path('service/GetId/', CommentServiceUser.as_view()),
]
