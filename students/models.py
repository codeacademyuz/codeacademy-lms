from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name  = models.CharField(max_length=255)
    last_name   = models.CharField(max_length=255)
    region      = models.ForeignKey(Region, on_delete=models.CASCADE)
    tg_username = models.CharField(max_length=255, unique=True)
    tg_chat_id  = models.CharField(max_length=255, unique=True)
    phone       = models.CharField(max_length=255, blank=True, null=True)
    github      = models.CharField(max_length=255, blank=True, null=True, unique=True)
    school      = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
