from django.shortcuts import render,HttpResponse
from rest_framework import viewsets,response
from rest_framework.decorators import action

from .models import Company,Employee
from .serializers import CompanySerializers,EmployeeSerializers
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializers

    # url for this method is "/companies/{company_id}/employees/"
    # Custom Api
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None): 

        try:
            comp=Company.objects.get(pk=pk)
            emps=Employee.objects.filter(company=comp)
            # WE have to sent json so use serializer
            emp_serializer=EmployeeSerializers(emps,many=True,context={'request':request})
            # Returning employees of company having company_id=pk
            return response.Response(emp_serializer.data)
        # if employe or company does not exist
        except Exception as e:
            return response.Response({'Error':'Query does not exist !!'})
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers
    