from django.db import models


class Course(models.Model):
    name = models.CharField(max_length==255, unique=True)

    def __str__(self):
        return self.name
    

class Assignment(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.name
