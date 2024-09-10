from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfileModel,PostModel

class UserRegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model=User
    fields=["username","password","email"]

class UserProfileSerializer(serializers.ModelSerializer):
  user=serializers.CharField(read_only=True)
  class Meta:
    model=UserProfileModel
    fields=['dob','gender','profile_pic','bio','user']

  def create(self, validated_data):
    user=self.context.get('user')
    print(user)
    return UserProfileModel.objects.create(user=user,**validated_data)

class PostSerializer(serializers.ModelSerializer):
  user=serializers.CharField(read_only=True)
  class Meta:
    model=PostModel
    fields=['image','caption','description','user']

