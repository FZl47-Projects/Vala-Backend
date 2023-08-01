from django.urls import path
from .views import TicketDetail,TicketList,TicketUser,TicketReplyDetail,TicketReplyList,TicketreplyeUser
 
from rest_framework.generics import ListCreateAPIView

urlpatterns = [
path('all/',TicketList.as_view()),   
path('GetId/<int:pk>/', TicketDetail.as_view()),
path('reply/GetId/<int:pk>/', TicketReplyDetail.as_view()),
path('reply/all/', TicketReplyList.as_view()),
path('GetId/', TicketUser.as_view()),
path('reply/GetId/', TicketreplyeUser.as_view()),
]
