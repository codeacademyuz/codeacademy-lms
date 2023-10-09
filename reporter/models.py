from django.db import models
from students.models import Student
from assignments.models import Task, Assignment


class Attempt(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attempts')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='attempts')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='attempts')
    attempts = models.IntegerField(default=1)
    is_correct = models.BooleanField()
    last_attempt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.student} - {self.task}'
