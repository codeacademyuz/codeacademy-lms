from rest_framework.serializers import ModelSerializer

from .models import Student, Group, Course, Homework


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'



class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'



class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'



class HomeworkSerializer(ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'

    def to_representation(self, ins):
        return {
            "group": {
                "id": ins.group.id,
                "name": ins.group.name,
            },
            "assignment": {
                "id": ins.assignment.id,
                "name": ins.assignment.name,
            },
        }
