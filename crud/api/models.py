from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField()
    roll_no = models.IntegerField()

    class Meta:
            verbose_name_plural = "Students"
            db_table            = 'student'   

