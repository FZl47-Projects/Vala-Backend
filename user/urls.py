from django.urls import path
from .views import UserDetail, UserList, UserUser, UserLogin, UserAuthLogin

from rest_framework.generics import ListCreateAPIView

urlpatterns = [
    path('all/', UserList.as_view()),
    path('GetId/<int:pk>/', UserDetail.as_view()),
    path('GetId/', UserUser.as_view()),
    path('Login/', UserLogin.as_view()),
    # NEW
    path('auth/login', UserAuthLogin.as_view()),
]
