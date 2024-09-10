from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app1.models import Student,Employee,Contact
from .serializers import StudetnSerializer,EmployeeSerializer,StudentModelSerializer,ContactModelSerializer
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework import status
from rest_framework import authentication, permissions


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


# Student views

class StudentListView(APIView):
  def get(self,request):
    students=Student.objects.all()
    serializer=StudetnSerializer(students,many=True)
    return Response(data=serializer.data)


class StudentCreateView(APIView):
  def post(self,request):
    stud_name=request.data.get("stud_name")
    email=request.data.get("email")
    phone=request.data.get("phone")
    Student.objects.create(stud_name=stud_name,email=email,phone=phone)
    return Response({"msg":"Student data created"})

class StudentDetailView(APIView):
  def get(self,request,*args,**kwargs):
    stud=Student.objects.get(id=kwargs.get("id"))
    serializer=StudetnSerializer(stud)
    return Response(data=serializer.data)

  def delete(self,request,*args,**kwargs):
    stud=Student.objects.get(id=kwargs.get("id"))
    stud.delete()
    return Response({"msg":f"Student '{stud.stud_name}' deteted"})

  def put(self,request,*args,**kwargs):
    stud=Student.objects.get(id=kwargs.get("id"))
    old_name=stud.stud_name
    stud_name=request.data.get("stud_name")
    email=request.data.get("email")
    phone=request.data.get("phone") 
    stud.stud_name=stud_name
    stud.email=email
    stud.phone=phone
    stud.save()
    return Response({"msg":f"'{old_name}' Updated to {stud_name}"})

# Employee Views

class EmployeeView(APIView):
  def get(self,request):
    emp=Employee.objects.all()
    serializer=EmployeeSerializer(emp,many=True)
    return Response(data=serializer.data)

  def post(self,request):
    emp_name=request.data.get("emp_name")
    email=request.data.get("email")
    phone=request.data.get("phone")
    salary=request.data.get("salary")
    designation=request.data.get("designation")
    Employee.objects.create(emp_name=emp_name,email=email,phone=phone,salary=salary,designation=designation)
    return Response({"msg":f"New Employe '{emp_name}' added"})

class EmployeeDetailView(APIView):
  def get(self,request,*args,**kwargs):
    emp=Employee.objects.get(id=kwargs.get("id"))
    serializer=EmployeeSerializer(emp)
    return Response(data=serializer.data)
  
  def put(self,request,*args,**kwargs):
    emp=Employee.objects.get(id=kwargs.get("id"))
    e_name=request.data.get("emp_name")
    phone=request.data.get("phone")
    email=request.data.get("email")
    salary=request.data.get("salary")
    designation=request.data.get("designation")
    emp.emp_name=e_name
    emp.email=email
    emp.phone=phone
    emp.salary=salary
    emp.designation=designation
    emp.save()
    return Response({"msg":f"Employee {kwargs.get("id")} Updated"})
  
  def delete(self,request,*args,**kwargs):
    emp=Employee.objects.get(id=kwargs.get("id"))
    emp.delete()
    return Response({"msg":f"Employee '{emp.emp_name}' Deleted"})
  



class StudentModelViewset(ModelViewSet):
  serializer_class=StudentModelSerializer
  queryset=Student.objects.all()


class ContactListView(ViewSet):
  authentication_classes=[authentication.BasicAuthentication]
  permission_classes=[permissions.IsAuthenticated]
  def list(self,request):
    contact=Contact.objects.all()
    serializer=ContactModelSerializer(contact,many=True)
    return Response(data=serializer.data)
  def create(self,request):
    serializer=ContactModelSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
      serializer.save()
      return Response(data=serializer.data)
    else:
      return Response(data=serializer.errors,status=status.HTTP_404_NOT_FOUND)
  def retrieve(self,request,*args,**kwargs):
    try:
      contact=Contact.objects.get(id=kwargs.get('pk'))
      serializer=ContactModelSerializer(contact)
      return Response(data=serializer.data)
    except:
      return Response({'msg':'Contact Not Found'})

  def update(self,request,*args,**kwargs):
    contact=Contact.objects.get(id=kwargs.get('pk'))
    serializer=ContactModelSerializer(data=request.data,instance=contact)
    print(serializer)
    if serializer.is_valid():
      serializer.save()
      return Response(data=serializer.data)


  def delete(self,request,*args,**kwargs):
    try:
      contact=Contact.objects.get(id=kwargs.get('pk'))
      contact.delete()
      return Response({'msg':'Contact deleted'})
    except:
      return Response({'msg':'Contact NOt Found'})


