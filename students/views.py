from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from assignments.models import Assignment
from .models import Student, Group, Course, Homework
from .serializers import StudentSerializer, GroupSerializer, CourseSerializer, HomeworkSerializer


class StudentView(APIView):
    def get(self, request: Request, pk=None):
        if pk is None:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)
        
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)

        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request: Request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request: Request, pk: int):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request: Request, pk: int):
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HomeworkView(APIView):
    def get(self, request: Request, assignment_id, group_id):

        try:
            assignment = Assignment.objects.get(id=assignment_id)
        except Assignment.DoesNotExist:
            return Response({"error": "course not found."})
        try:
            group = Group.objects.get(id=group_id)
        except Group.DoesNotExist:
            return Response({"error": "course not found."})

        homeworks = Homework.objects.filter(assignment=assignment, group=group)
        serializer = HomeworkSerializer(homeworks, many=True)
        return Response(serializer.data)


class CourseView(APIView):
    def get(self, request: Request):

        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class GroupView(APIView):
    def get(self, request: Request, pk: int):
        try:
            course = Course.objects.get(id=pk)
        except Course.DoesNotExist:
            return Response({"error": "course not found."})

        groups = Group.objects.filter(course=course)
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)
    