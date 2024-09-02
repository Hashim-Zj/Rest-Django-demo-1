from django.db import models

# Create your models here.
class Student(models.Model):
  stud_name=models.CharField(max_length=100)
  email=models.EmailField()
  phone=models.IntegerField()
  

class Employee(models.Model):
  emp_name=models.CharField(max_length=100)
  email=models.EmailField()
  phone=models.IntegerField()
  salary=models.IntegerField()
  designation=models.CharField(max_length=50)


class Contact(models.Model):
  name=models.CharField(max_length=100)
  email=models.EmailField()
  phone=models.IntegerField()

  
