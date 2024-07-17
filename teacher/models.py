from django.db import models

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
    



















