from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from .seraializers import UserRegisterSerializer,UserProfileSerializer,PostSerializer,CommentSerializer
from django.contrib.auth.models import User
from .models import UserProfileModel,PostModel,CommentsModel
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework.decorators import action

class UserRegisterView(ViewSet):
  def create(self,request):
    serializer=UserRegisterSerializer(data=request.data)
    if serializer.is_valid():
      uname=serializer.validated_data.get("username") # type: ignore
      psw=serializer.validated_data.get("password") # type: ignore
      email=serializer.validated_data.get("email") # type: ignore
      User.objects.create_user(username=uname,password=psw,email=email) # type: ignore
      return Response(data=serializer.data)
    else:
      return Response(data=serializer.errors)

class UserProfileView(ModelViewSet):
  authentication_classes=[authentication.TokenAuthentication]
  permission_classes=[permissions.IsAuthenticated]

  serializer_class=UserProfileSerializer
  queryset=UserProfileModel.objects.all()

  def create(self,request,*args,**kwargs):
    serializer=UserProfileSerializer(data=request.data,context={'user':request.user})
    print(serializer)
    if serializer.is_valid():
      serializer.save()
      return Response(data=serializer.data)
    else:
      return Response(data=serializer.errors)
  
  
  @action(methods=["POST"],detail=True)   #detail using by to add data to pass to urls
  def add_followers(self,request,*args,**kwargs):
    id=kwargs.get('pk')
    user_to_follw=UserProfileModel.objects.get(id=id)
    print(user_to_follw)
    user_to_follw.follwers.add(request.user)
    return Response({'msg':'followed'})


class PostView(ModelViewSet):
  authentication_classes=[authentication.TokenAuthentication]
  permission_classes=[permissions.IsAuthenticated]

  serializer_class=PostSerializer
  queryset=PostModel.objects.all()

  def perform_create(self,serializer):
    return serializer.save(user=self.request.user)

  @action(methods=['POST'],detail=True)
  def add_likes(self,request,*args,**kwargs):
    id=kwargs.get('pk')
    post_to_like=PostModel.objects.get(id=id)
    post_to_like.likes.add(request.user)
    return Response({'msg':'post liked'})

  @action(methods=['POST'],detail=True)
  def add_comments(self,request,*args,**kwargs):
    post=PostModel.objects.get(id=kwargs.get('pk'))
    user=request.user
    comment=CommentSerializer(data=request.data,context={'user':user,'post':post})
    if comment.is_valid():
      comment.save()
      return Response(data=comment.data)
    
  @action(methods=['GET'],detail=True)
  def list_commetns(self,request,*args,**kwargs):
    post=PostModel.objects.get(id=kwargs.get('pk'))
    commets=CommentsModel.objects.filter(post=post)
    serializer=CommentSerializer(commets,many=True)
    return Response(data=serializer.data)