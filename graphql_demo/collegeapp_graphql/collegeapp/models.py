from django.db import models


class University(models.Model):
    # Class to build model for University 
    # with name of university as column
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    # Class to build model for Student with
    # first_name,last_name,university as fields
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
