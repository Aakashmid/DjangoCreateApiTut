from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .models import Company,Employee
from .serializers import CompanySerializers,EmployeeSerializers
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializers


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers
    