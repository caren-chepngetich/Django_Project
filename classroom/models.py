from django.db import models

class ClassRoom(models.Model):
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

