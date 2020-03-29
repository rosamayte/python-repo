from rest_framework import serializers
from .models import Project, Student


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'medium_url',
            'description',
        )
        model = Project


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'age',
            'roll_number',
            'created_at',
            'updated_at'
        )
        model = Student
