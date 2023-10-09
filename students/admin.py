from django.contrib import admin
from .models import Student, Group, Course, Homework


admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Course)
admin.site.register(Homework)
