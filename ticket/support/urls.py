from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('users/', UserList.as_view()),
    path('show_tickets/', DetailTicket.as_view()),
    path('create_ticket/', UserTicket.as_view()),
    path('ticket/<int:pk>/', UserTicket.as_view()),
    path('tickets/<int:pk>', AdminRedactor.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)