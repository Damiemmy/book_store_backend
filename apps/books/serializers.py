from rest_framework import serializers
from .models import Book, Category, Author


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    author = AuthorSerializer(read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True
    )

    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        source="author",
        write_only=True
    )

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "description",
            "price",
            "stock",
            "cover_image",
            "category",
            "author",
            "category_id",
            "author_id",
            "created_at",
        ]

