from django.db import models

# Create your models here.

class Teacher(models.Model):
    name=models.CharField(max_lenght=30)
    email=models.EmailField(unique=True)
    teacher_id=models.CharField(max_length=20)
    password=models.CharField(max_length=15)
    department=models.CharField(max_length=30)

class Student(models.Model):
    name=models.CharField(max_length=30)
    Class=models.CharField(max_length=20)
    department=models.CharField(max_length=30)
    register_id=models.CharField(max_length=20)
    mobile=models.IntegerField(max_length=10,null=False)
    email=models.EmailField(unique=True)
    parent=models.CharField(max_length=30)
    parent_no=models.IntegerField(max_length=10,null=False)
    password=models.CharField(max_length=15)
    


