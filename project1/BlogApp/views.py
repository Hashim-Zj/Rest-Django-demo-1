from django.shortcuts import render
from .serializers import BlogModelSerializer,UserRegister
from .models import BlogModel
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import authentication, permissions


# IsAuthenticated 
# IsAdminUser

class BlogModelViewsetView(ModelViewSet):
  # authentication_classes=[authentication.BasicAuthentication]
  authentication_classes=[authentication.TokenAuthentication]
  permission_classes=[permissions.IsAuthenticated]
  # permission_classes=[permissions.IsAdminUser]
  serializer_class=BlogModelSerializer
  queryset=BlogModel.objects.all()


class UserRegisterView(ViewSet):
  def create(self,request):
    serializer=UserRegister(data=request.data)
    if serializer.is_valid():
      print(serializer.validated_data)
      name=serializer.validated_data.get('username') # type: ignore
      psw=serializer.validated_data.get('password') # type: ignore
      email=serializer.validated_data.get('email') # type: ignore
      User.objects.create_user(username=name,password=psw,email=email) # type: ignore
      return Response({'msg':"data add"})
    
