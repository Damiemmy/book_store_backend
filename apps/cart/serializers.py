from rest_framework import serializers
from .models import Cart,CartItem
from apps.books.models import Book

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields=["id","quantity","book"]

class CartSerializer(serializers.ModelSerializer):
    items=CartItemSerializer(many=True,read_only=True)
    class Meta:
        model=Cart
        fields=["id","user","items","created_at"]
        read_only_fields=["user"]