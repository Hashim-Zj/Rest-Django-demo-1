from django.shortcuts import render
from .serializers import BlogModelSerializer,UserRegister
from .models import BlogModel
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User



class BlogModelViewsetView(ModelViewSet):
  serializer_class=BlogModelSerializer
  queryset=BlogModel.objects.all()


class UserRegisterView(ViewSet):
  def create(self,request):
    serializer=UserRegister(data=request.data)
    if serializer.is_valid():
      print(serializer.validated_data)
      uname=serializer.validated_data.get('username')
      psw=serializer.validated_data.get('password')
      email=serializer.validated_data.get('email')
      User.objects.create_user(username=uname,password=psw,email=email)
      return Response({'msg':"data add"})