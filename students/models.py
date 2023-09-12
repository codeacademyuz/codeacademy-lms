from django.db import models
from assignments.models import Course


class Student(models.Model):
    first_name  = models.CharField(max_length=255)
    last_name   = models.CharField(max_length=255)
    tg_username = models.CharField(max_length=255, unique=True)
    tg_chat_id  = models.CharField(max_length=255, unique=True)
    phone       = models.CharField(max_length=255, blank=True, null=True)
    github      = models.CharField(max_length=255, blank=True, null=True, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    students = models.ManyToManyField(Student)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name