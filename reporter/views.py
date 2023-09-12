from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import Attempt
from assignments.models import Assignment, Task
from students.models import Student, Group


class AttemptView(APIView):
    def post(self, request: Request) -> Response:
        data = request.data

        github = data.get('github')
        task = data.get('task')
        assignment = data.get('assignment')
        is_correct = data.get('is_correct')

        if not isinstance(github, str): 
            return Response({'error': 'github username error'}, status=status.HTTP_404_NOT_FOUND)

        if not isinstance(task, str): 
            return Response({'error': 'task name error'}, status=status.HTTP_404_NOT_FOUND)

        if not isinstance(assignment, str): 
            return Response({'error': 'assignment name error'}, status=status.HTTP_404_NOT_FOUND)

        if not isinstance(is_correct, bool): 
            return Response({'error': 'is correct error'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            assignment = Assignment.objects.get(name=assignment)
        except Assignment.DoesNotExist:
            return Response({'error': 'assignment not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            task = assignment.tasks.get(name=task)
        except Task.DoesNotExist:
            return Response({'error': 'task not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            student = Student.objects.get(github=github)
        except Task.DoesNotExist:
            return Response({'error': 'student not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            attempt = Attempt.objects.get(
                student=student,
                assignment=assignment,
                task=task,
            )
            attempt.is_correct = is_correct
            attempt.attempts += 1
            attempt.save()
        except Attempt.DoesNotExist:
            attempt = Attempt.objects.create(
                student=student,
                assignment=assignment,
                task=task,
                is_correct=is_correct,
                attempts=1
            )
            attempt.save()

        return Response({'success': True}, status=status.HTTP_201_CREATED)


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


class ReporterByGroupName(APIView):
    def get(self, request: Request) -> Response:
        assignement_name = request.query_params.get('assignment_name')
        group_name = request.query_params.get('group_name')
        
        if assignement_name is None:
            return Response({'error': 'assignment_name query params required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if group_name is None:
            return Response({'error': 'group_name query params required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            assignment = Assignment.objects.get(name=assignement_name)
        except Assignment.DoesNotExist:
            return Response({'error': 'assignment not found'}, status=status.HTTP_404_NOT_FOUND)

        try:
            group = Group.objects.get(name=group_name)
        except Group.DoesNotExist:
            return Response({'error': 'group not found'}, status=status.HTTP_404_NOT_FOUND)

        students = group.students.all()
        tasks = assignment.tasks.all()

        result = []
        for student in students:
            student_result = {
                'first_name': student.first_name,
                'last_name': student.last_name,
                'github': student.github,
                'tasks': []
            }
            attempts = student.attempts.filter(assignment=assignment).all()
            for task in tasks:
                last_attempt = attempts.filter(task=task)
                if last_attempt:
                    student_result['tasks'].append({"name": task.name, "attempts": last_attempt.last().attempts, "is_correct": last_attempt.last().is_correct})
                else:
                    student_result['tasks'].append({"name": task.name, "attempts": 0, "is_correct": False})
            result.append(student_result)

        return Response(result)
