from django.db import models

# Create your models here.

class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key = True)
    DepartmentName = models.CharField(max_length=100, unique = True)

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key = True)
    EmployeeName = models.CharField(max_length=100, unique = True)
    Department = models.CharField(max_length=100)
    DateOfJoint = models.DateField()
    PhotoFileName = models.CharField(max_length=100)

class Students(models.Model):
    StudentId = models.AutoField(primary_key = True)
    StudentName = models.CharField(max_length=100)
    Employee = models.ForeignKey(Employees, to_field = "EmployeeName", on_delete = models.CASCADE)
    StudentYear = models.IntegerField()

class Courses(models.Model):
    CourseId = models.AutoField(primary_key = True)
    CourseName = models.CharField(max_length=100)
    Employee = models.ForeignKey(Employees, to_field = "EmployeeName", on_delete = models.CASCADE)

