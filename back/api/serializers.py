from rest_framework import serializers 
from api.models import Departments, Employees, Students, Courses


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentId',
                    'DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId', 
                    'EmployeeName', 
                    'Department', 
                    'DateOfJoint',
                    'PhotoFileName')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('StudentId', 
                    'StudentName', 
                    'Employee',
                    'StudentYear',
                )

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = (
            'CourseId',
            'CourseName',
            'Employee',
        )