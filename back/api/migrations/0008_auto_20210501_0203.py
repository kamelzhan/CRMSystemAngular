# Generated by Django 3.2 on 2021-04-30 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_students_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='DepartmentName',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='EmployeeName',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='Department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.departments', to_field='DepartmentName'),
        ),
        migrations.AlterField(
            model_name='students',
            name='Employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.employees', to_field='EmployeeName'),
        ),
    ]