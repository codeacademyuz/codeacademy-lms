from django.db import models
from assignments.models import Assignment


class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    

class Student(models.Model):
    first_name  = models.CharField(max_length=255)
    last_name   = models.CharField(max_length=255)
    github      = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    students = models.ManyToManyField(Student, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Homework(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.assignment.name
