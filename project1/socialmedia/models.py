from django.db import models
from django.contrib.auth.models import User


class UserProfileModel(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
  bio=models.CharField(max_length=100)
  dob=models.DateField(null=True)
  options=(
    ('male','male'),
    ('female','female'),
    ('others','others'))
  gender=models.CharField(max_length=100,choices=options)
  profile_pic=models.ImageField(upload_to='media/profile')
  follwers=models.ManyToManyField(User,related_name='followers')

class PostModel(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  image=models.ImageField(upload_to='media/post')
  caption=models.TextField(max_length=100)
  date=models.DateField(auto_now_add=True)
  description=models.TextField()
  likes=models.ManyToManyField(User,related_name='likes')