from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import Attempt
from assignments.models import Assignment, Task
from students.models import Student


class AttemptView(APIView):
    def post(self, request: Request) -> Response:
        data = request.data

        tg_username = data.get('tg_username')
        assignment_name = data.get('assignment_name')
        task_name = data.get('task_name')
        is_correct = data.get('is_correct')

        if not all([tg_username, assignment_name, task_name, is_correct]):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            student = Student.objects.get(tg_username=tg_username)
            assignment = Assignment.objects.get(name=assignment_name)
            task = assignment.tasks.get(name=task_name)

        except (Student.DoesNotExist, Assignment.DoesNotExist, Task.DoesNotExist):
            return Response(status=status.HTTP_404_NOT_FOUND)

        attempt = Attempt.objects.create(
            student=student,
            assignment=assignment,
            task=task,
            is_correct=is_correct
        )

        return Response(status=status.HTTP_201_CREATED)


class ReporterView(APIView):
    def get(self, request: Request) -> Response:
        assignement_name = request.query_params.get('assignment_name')
        
        if assignement_name is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            assignment = Assignment.objects.get(name=assignement_name)
        except Assignment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        students = Student.objects.all()
        tasks = Task.objects.filter(assignment=assignment)

        result = []
        for student in students:
            student_result = {
                'student': {
                    'first_name': student.first_name,
                    'last_name': student.last_name,
                    'tg_username': student.tg_username,
                    'region': student.region.name,
                    'phone': student.phone,
                    'github': student.github,
                    'school': student.school
                },
                'tasks': []
            }
            for task in tasks:
                attempts = Attempt.objects.filter(
                    student=student,
                    task=task
                ).order_by('-created_at')
                
                if attempts.exists():
                    attempt = attempts.first()
                    student_result['tasks'].append({
                        'task_name': task.name,
                        'is_correct': attempt.is_correct,
                        'attepts_count': attempts.count(),
                    })
                else:
                    student_result['tasks'].append({
                        'task_name': task.name,
                        'is_correct': False,
                        'attepts_count': 0,
                    })
            result.append(student_result)

        return Response(result)


class ReporterByRegion(APIView):
    def get(self, request: Request) -> Response:
        assignement_name = request.query_params.get('assignment_name')
        region = request.query_params.get('assignment_name')
        
        if assignement_name is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            assignment = Assignment.objects.get(name=assignement_name)
        except Assignment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        students = Student.objects.filter(region=region)
        tasks = Task.objects.filter(assignment=assignment)

        result = []
        for student in students:
            student_result = {
                'student': {
                    'first_name': student.first_name,
                    'last_name': student.last_name,
                    'tg_username': student.tg_username,
                    'region': student.region.name,
                    'phone': student.phone,
                    'github': student.github,
                    'school': student.school
                },
                'tasks': []
            }
            for task in tasks:
                attempts = Attempt.objects.filter(
                    student=student,
                    task=task
                ).order_by('-created_at')
                
                if attempts.exists():
                    attempt = attempts.first()
                    student_result['tasks'].append({
                        'task_name': task.name,
                        'is_correct': attempt.is_correct,
                        'attepts_count': attempts.count(),
                    })
                else:
                    student_result['tasks'].append({
                        'task_name': task.name,
                        'is_correct': False,
                        'attepts_count': 0,
                    })
            result.append(student_result)

        return Response(result)