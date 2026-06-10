from django.shortcuts import render
from .models import Book
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer
from rest_framework.filters import OrderingFilter,SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import  IsAdminOrReadOnly


class BookViewSet(ModelViewSet):
    queryset = Book.objects.select_related("category", "author")
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]
    backend_filters=[OrderingFilter,SearchFilter,DjangoFilterBackend]
    search_fields = ["title", "description"]
    filterset_fields = ["category", "author__name"]
    ordering_fields = ["price", "created_at"]