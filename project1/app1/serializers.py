from rest_framework import serializers


class StudetnSerializer(serializers.Serializer):
  stud_name=serializers.CharField(max_length=100)
  email=serializers.EmailField()
  phone=serializers.IntegerField()
  