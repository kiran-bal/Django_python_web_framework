from rest_framework import serializers
from .models import University, Student


class UniversitySerializer(serializers.ModelSerializer):
    """Class to convert data from model to json"""
    class Meta:
        model = University
        fields = ('name',)  # field to enter university name


class StudentSerializer(serializers.ModelSerializer):
    """Class to convert data from model to json"""
    class Meta:
        model = Student
        # Four fields will be created to input data
        fields = ('first_name', 'last_name', 'university')
