from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .serializers import RegisterSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView,RetrieveAPIView
from .jwt import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from apps.notifications.tasks import (
    send_welcome_email_task
)

User=get_user_model()

# Create your views here.

class RegisterView(CreateAPIView):
    serializer_class=RegisterSerializer

    def perform_create(self,serializer):
        user = serializer.save()
        send_welcome_email_task.delay(
            user.email,
            user.username,
        )

class LoginView(TokenObtainPairView):
    serializer_class=CustomTokenObtainPairSerializer

class UserProfileView(RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user =request.user

        return Response({
            "id":user.id,
            "username":user.username,
            "email":user.email,
            "role":user.role,
            
        })



