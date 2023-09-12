from rest_framework.serializers import ModelSerializer

from .models import Student, Group


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'



class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
