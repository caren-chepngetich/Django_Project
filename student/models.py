from typing import Any
from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    code = models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    country = models.CharField(max_length = 20)
    bio= models.TextField()
    def __str__(self):
        return f"{self.first_name}{self.last_name}"

class Class(models.Model):
    class_name =  models.CharField(max_length=20)  
    course = models.CharField()
    class_capacity = models.IntegerField()
    teacher = models.CharField()
    location = models.CharField()
    room_number = models.PositiveSmallIntegerField()
    class_time = models.CharField()
    class_id = models.PositiveSmallIntegerField()
    student_names = models.TextField()
    class_days = models.SmallIntegerField()

class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    nationality = models.CharField()
    department = models.CharField()
    course = models.CharField()
    gender = models.CharField()
    bank_account_number = models.CharField()
    teacher_id = models.PositiveSmallIntegerField()
    date_of_joining = models.DateField()
    
class Course(models.Model):
    course_id = models.PositiveSmallIntegerField()
    department = models.CharField()
    course_description = models.TextField()
    class_hours = models.DurationField()
    course_instructor = models.CharField()
    assessment_requirements = models.TextField()
    course_capacity = models.PositiveSmallIntegerField()
    grade_level = models.CharField()
    school_term = models.PositiveSmallIntegerField()



















