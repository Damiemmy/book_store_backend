from django.shortcuts import render

# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView
from .jwt import CustomTokenObtainPairSerializer
from .serializers import RegisterationSerializer
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,RetrieveAPIView
from rest_framework.permissions import IsAuthenticated


class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class RegisterView(CreateAPIView):
    serializer_class=RegisterationSerializer

class UserProfileView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        user=request.user

        return Response({
            "username":user.username,
            "email":user.email,
            "role": user.role,
        })



