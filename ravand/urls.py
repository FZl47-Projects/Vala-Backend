from django.urls import path
from .views import RavandDetail,RavandList,RavandUser,ImageRavandDetail,ImageRavandList
 
from rest_framework.generics import ListCreateAPIView

urlpatterns = [
path('all/',RavandList.as_view()),   
path('GetId/<int:pk>/', RavandDetail.as_view()),
path('image/all/',ImageRavandList.as_view()),   
path('image/GetId/<int:pk>/', ImageRavandDetail.as_view()),
path('GetId/', RavandUser.as_view()),

]
