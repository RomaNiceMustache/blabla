from django.shortcuts import render
from .serializers import *
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .permissions import *


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserTicket(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DetailTicket(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class AdminRedactor(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = AdminSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly,
                           permissions.IsAdminUser]