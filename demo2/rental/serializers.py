from rest_framework import serializers
from . import models

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ('id','name','college')

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Library
        fields = ('id','book_name','author')
class BorrowedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Borrowed
        fields = ('id','mybook','person','bookdate','returndate')