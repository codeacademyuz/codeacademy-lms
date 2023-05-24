from rest_framework.serializers import ModelSerializer

from .models import Student, Region


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class RegionSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'
