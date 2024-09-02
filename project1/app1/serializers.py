from rest_framework import serializers
from .models import Student,Contact



class StudetnSerializer(serializers.Serializer):
  id=serializers.IntegerField(read_only=True)
  stud_name=serializers.CharField(max_length=100)
  email=serializers.EmailField()
  phone=serializers.IntegerField()
  

class EmployeeSerializer(serializers.Serializer):
  id=serializers.IntegerField(read_only=True)
  emp_name=serializers.CharField(max_length=100)
  email=serializers.EmailField()
  phone=serializers.IntegerField()
  salary=serializers.IntegerField()
  designation=serializers.CharField(max_length=50)

class StudentModelSerializer(serializers.ModelSerializer):
  class Meta:
    model=Student
    fields="__all__"


class ContactModelSerializer(serializers.ModelSerializer):
  class Meta:
    model=Contact
    fields="__all__"

    