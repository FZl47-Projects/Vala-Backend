from django.urls import path
from .views import AnalyzeDetail,AnalyzeList,AnalyzeUser
 
from rest_framework.generics import ListCreateAPIView

urlpatterns = [
path('all/',AnalyzeList.as_view()),   
path('GetId/<int:pk>/', AnalyzeDetail.as_view()),
path('GetId/', AnalyzeUser.as_view()),

]
