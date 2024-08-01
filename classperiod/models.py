from django.db import models

class ClassPeriod(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    course = models.CharField(max_length=100)  
    day_of_the_week = models.CharField(max_length=20)  
    total_students = models.PositiveIntegerField()
    trainer_name = models.CharField(max_length=100)  
    trainers_assistant_name = models.CharField(max_length=100)  
    number_of_hours = models.DurationField()
