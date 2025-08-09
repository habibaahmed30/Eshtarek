from django.shortcuts import render
from rest_framework import generics,permissions
from .serializers import RegistrationSerializer


# Create your views here.

class RegisterView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]

