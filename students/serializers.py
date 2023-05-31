from rest_framework.serializers import ModelSerializer

from .models import Student, Region, Group


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class RegionSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')
