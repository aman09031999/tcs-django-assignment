from django.db import models

# Create your models here.
class Student(models.Model):
    r_no = models.IntegerField()
    name = models.CharField(max_length=100)
    dob = models.DateField()
    marks = models.FloatField()
