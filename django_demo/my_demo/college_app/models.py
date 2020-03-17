""" Creates two models University and Student"""
from django.db import models


class University(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"

    def __str__(self):
        # Returns the name of University when called
        # instead of  object itself
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    class meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __unicode__(self):
        # Returns full name when called instead of
        # returning the object itself
        return '%s %s' % (self.first_name, self.last_name)
