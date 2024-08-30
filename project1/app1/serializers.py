from rest_framework import serializers


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

  