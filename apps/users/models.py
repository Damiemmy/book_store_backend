from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    USER_ROLE=(
        ("admin","Admin"),
        ("customer","Customer")
    )

    email=models.EmailField(unique=True)
    provider=models.CharField(max_length=20,default='email')
    avatar=models.URLField(blank=True,null=True)
    role=models.CharField(max_length=20,choices=USER_ROLE,default='customer')

    def __str__(self):
        return self.username

