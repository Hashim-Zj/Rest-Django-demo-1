from django.db import models

# Create your models here.
class Student(models.Model):
  stud_name=models.CharField(max_length=100)
  email=models.EmailField()
  phone=models.IntegerField()
  