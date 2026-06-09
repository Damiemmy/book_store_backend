from rest_framework import serializers
from django.contrib.auth import get_user_model
User=get_user_model

class RegisterationSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,min_length=8)

    class Meta:
        model=User
        field=['username','email','password']

    def create(self,validated_data):
        user=User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validate_data["email"],
        )
        return user

    def validate_email(self,value):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('user already exists in database')
        return value

    
