from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .models import Company
from .serializers import CompanySerializers
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializers
