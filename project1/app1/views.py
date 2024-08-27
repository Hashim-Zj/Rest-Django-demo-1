from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app1.models import Student
from .serializers import StudetnSerializer


# Create your views here.
class Home(APIView):
  def get(self,request):
    print("welcome")
    n1=request.data.get("n1")
    n2=request.data.get("n2")
    print(n1+n2)
    return Response(n1+n2)


class Factorial(APIView):
  def get(self,request):
    print("Factorial is:")
    n=request.data.get("n")
    fact=1
    for i in range(1,n+1,):
      print(i)
      fact*=i
    return Response(fact)

class StudentListView(APIView):
  def get(self,request):
    students=Student.objects.all()
    # print(students)
    serializer=StudetnSerializer(students,many=True)
    # print(type(serializer))
    return Response(data=serializer.data)


class StudentCreateView(APIView):
  def post(self,request):
    stud_name=request.data.get("stud_name")
    email=request.data.get("email")
    phone=request.data.get("phone")
    Student.objects.create(stud_name=stud_name,email=email,phone=phone)
    return Response({"msg":"Student data created"})
