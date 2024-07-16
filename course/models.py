from django.db import models

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

