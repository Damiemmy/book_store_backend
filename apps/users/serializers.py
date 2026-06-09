from rest_framework import serializers
from .models import User

class RegisterationSerializer(serializers.ModelSerializer):
    password=serializers.CharField(read_only=True)

    def create(self,validated_data):
        user=Users.objects.create_user(**validated_data)
        user.save()