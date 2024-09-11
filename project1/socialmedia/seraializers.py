from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfileModel,PostModel,CommentsModel

class UserRegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model=User
    fields=["username","password","email"]

class UserProfileSerializer(serializers.ModelSerializer):
  user=serializers.CharField(read_only=True)
  list_followers=serializers.CharField(read_only=True)
  class Meta:
    model=UserProfileModel
    fields=['dob','gender','profile_pic','bio','user','list_followers']

  def create(self, validated_data):
    user=self.context.get('user')
    print(user)
    return UserProfileModel.objects.create(user=user,**validated_data)

class CommentSerializer(serializers.ModelSerializer):
  user=serializers.CharField(read_only=True)
  post=serializers.CharField(read_only=True)
  class Meta:
    model=CommentsModel
    fields='__all__'

  def create(self, validated_data):
    user=self.context.get('user')
    post=self.context.get('post')
    return CommentsModel.objects.create(user=user,post=post,**validated_data)

class PostSerializer(serializers.ModelSerializer):
  user=serializers.CharField(read_only=True)
  likes_cound=serializers.CharField(read_only=True)
  comments_count=serializers.CharField(read_only=True)
  comments_view=CommentSerializer(read_only=True,many=True)
  class Meta:
    model=PostModel
    fields=['image','caption','description','user','likes_cound','comments_count','comments_view']
