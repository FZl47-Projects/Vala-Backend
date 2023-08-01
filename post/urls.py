from django.urls import path
from .views import PostDetail,PostList,PostUser,CategoryDetail,CategoryList
 
from rest_framework.generics import ListCreateAPIView

urlpatterns = [
path('all/',PostList.as_view()),   
path('GetId/<int:pk>/', PostDetail.as_view()),
path('GetId/', PostUser.as_view()),
path('category/all/',CategoryList.as_view()),   
path('category/GetId/<int:pk>/', CategoryDetail.as_view()),
]
