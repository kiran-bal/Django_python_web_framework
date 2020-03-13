from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.name

class Library(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.book_name

class Borrowed(models.Model):
    mybook = models.ForeignKey(Library,on_delete=models.CASCADE)
    person = models.ForeignKey(Student,on_delete=models.CASCADE)
    bookdate = models.DateTimeField(null=True)
    returndate = models.DateTimeField(null=True, blank=True)
