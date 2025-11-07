from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Doctor
from .serializers import DoctorSerializer



class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by('id')
    serializer_class = DoctorSerializer
   


