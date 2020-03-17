from django.shortcuts import render
from rest_framework import viewsets
from .models import University, Student
from .serializers import UniversitySerializer, StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """ Class to combine student fields view"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class UniversityViewSet(viewsets.ModelViewSet):
    """Class to combine university fields view"""
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
