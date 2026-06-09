from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import LoginView,RegisterView,UserProfileView

urlpatterns = [
    path("login/", LoginView.as_view(),name='login'),
    path("register/", RegisterView.as_view(),name='register'),
    path("refresh/", TokenRefreshView.as_view()),
    path("profile/", TokenRefreshView.as_view()),
]