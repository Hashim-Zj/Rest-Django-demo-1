from rest_framework import serializers
from .models import BlogModel
from django.contrib.auth.models import User


class BlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = "__all__"


class UserRegister(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']
