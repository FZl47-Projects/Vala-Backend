# from django.urls import path
# from .views import CortexList,CortexDetail,CortexUser,oprator_laserList,oprator_laserDetail,oprator_laserUser,DistrictList
 
# from rest_framework.generics import ListCreateAPIView

# urlpatterns = [
# path('all/',CortexList.as_view()),   
# path('GetId/<int:pk>/', CortexDetail.as_view()),
# path('GetId/', CortexUser.as_view()),

# path('op/all/',oprator_laserList.as_view()),   
# path('op/GetId/<int:pk>/', oprator_laserDetail.as_view()),
# path('op/GetId/', oprator_laserUser.as_view()),
# path('district/all/',DistrictList.as_view()),   
# ]


# NEW
from django.urls import path
from . import views

app_name = 'cortex'
urlpatterns = [
    path('district',views.District.as_view()),
    path('district/<int:pk>',views.DistrictDetail.as_view()),

    path('user/<int:user_id>',views.CortextUser.as_view()),

    path('operator',views.Operator.as_view()),
]