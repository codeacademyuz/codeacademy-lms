from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import Student, Region
from .serializers import StudentSerializer, RegionSerializer


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
        region = request.data.get('region')
        if region is not None:
            try:
                region = Region.objects.get(name=region)
            except Region.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

            data = {
                "first_name": request.data.get('first_name'),
                "last_name": request.data.get('last_name'),
                "tg_username": request.data.get('tg_username'), 
                "tg_chat_id": request.data.get('tg_chat_id'),
                "phone": request.data.get('phone'),
                "school": request.data.get('school'), 
                "region": region.id
            }

            serializer = StudentSerializer(data=data)
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


class StudentByRegionView(APIView):
    def get(self, request: Request, region_id: int):
        try:
            region = Region.objects.get(pk=region_id)
        except Region.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        students = region.students.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
