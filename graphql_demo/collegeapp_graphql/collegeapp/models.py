from django.db import models

class University(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s"% (self.first_name,self.last_name)

    
