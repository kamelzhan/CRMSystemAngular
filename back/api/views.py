from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import APIView
from api.models import Departments, Employees, Students, Courses
from api.serializers import DepartmentSerializer, EmployeeSerializer, StudentSerializer, CourseSerializer
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
# Create your views here.

class DepartmentAPIClassView(APIView):
    @csrf_exempt
    def departmentApi(request, id = 0):
        if request.method == 'GET':
            departments = Departments.objects.all()
            departments_serializer = DepartmentSerializer(departments, many = True)
            return JsonResponse(departments_serializer.data, safe = False)
        elif request.method == 'POST':
            department_data = JSONParser().parse(request)
            department_serializer = DepartmentSerializer(data = department_data)
            if department_serializer.is_valid():
                department_serializer.save()
                return JsonResponse("Added Successfully!", safe = False)
            return JsonResponse("Failed to add", safe = False)
        elif request.method == 'PUT':
            department_data = JSONParser().parse(request)
            department = Departments.objects.get(DepartmentId = department_data['DepartmentId'])
            department_serializer = DepartmentSerializer(department, data = department_data)
            if department_serializer.is_valid():
                department_serializer.save()
                return JsonResponse("Updated Successfully!", safe = False)
            return JsonResponse("Failed to update", safe = False)
        elif request.method == 'DELETE':
            department = Departments.objects.get(DepartmentId = id)
            department.delete()
            return JsonResponse("Deleted Successfully!", safe = False)


class EmployeeAPIClassView(APIView):
    @csrf_exempt
    def employeeApi(request, id = 0):
        if request.method == 'GET':
            employees = Employees.objects.all()
            employees_serializer = EmployeeSerializer(employees, many = True)
            return JsonResponse(employees_serializer.data, safe = False)
        elif request.method == 'POST':
            employee_data = JSONParser().parse(request)
            employee_serializer = EmployeeSerializer(data = employee_data)
            if employee_serializer.is_valid():
                employee_serializer.save()
                return JsonResponse("Added Successfully!", safe = False)
            return JsonResponse("Failed to add", safe = False)
        elif request.method == 'PUT':
            employee_data = JSONParser().parse(request)
            employee = Employees.objects.get(EmployeeId = employee_data['EmployeeId'])
            employee_serializer = EmployeeSerializer(employee, data = employee_data)
            if employee_serializer.is_valid():
                employee_serializer.save()
                return JsonResponse("Updated Successfully!", safe = False)
            return JsonResponse("Failed to update", safe = False)
        elif request.method == 'DELETE':
            employee = Employees.objects.get(EmployeeId = id)
            employee.delete()
            return JsonResponse("Deleted Successfully!", safe = False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe = False)


@csrf_exempt
def studentApi(request, id = 0):
    if request.method == 'GET':
        students = Students.objects.all()
        student_serializer = StudentSerializer(students, many = True)
        return JsonResponse(student_serializer.data, safe = False)
    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(data = student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Added Successfully!", safe = False)
        return JsonResponse("Failed to add", safe = False)
    elif request.method == 'PUT':
        student_data = JSONParser().parse(request)
        student = Students.objects.get(StudentId = student_data['StudentId'])
        student_serializer = StudentSerializer(student, data = student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse("Updated Successfully!", safe = False)
        return JsonResponse("Failed to update", safe = False)
    elif request.method == 'DELETE':
        student = Students.objects.get(StudentId = id)
        student.delete()
        return JsonResponse("Deleted Successfully!", safe = False)


@csrf_exempt
def courseApi(request, id = 0):
    if request.method == 'GET':
        course = Courses.objects.all()
        course_serializer = CourseSerializer(course, many = True)
        return JsonResponse(course_serializer.data, safe = False)
    elif request.method == 'POST':
        course_data = JSONParser().parse(request)
        course_serializer = CourseSerializer(data = course_data)
        if course_serializer.is_valid():
            course_serializer.save()
            return JsonResponse("Added Successfully!", safe = False)
        return JsonResponse("Failed to add", safe = False)
    elif request.method == 'PUT':
        course_data = JSONParser().parse(request)
        course = Courses.objects.get(CourseId = course_data['CourseId'])
        course_serializer = CourseSerializer(course, data = course_data)
        if course_serializer.is_valid():
            course_serializer.save()
            return JsonResponse("Updated Successfully!", safe = False)
        return JsonResponse("Failed to update", safe = False)
    elif request.method == 'DELETE':
        course = Courses.objects.get(CourseId = id)
        course.delete()
        return JsonResponse("Deleted Successfully!", safe = False)