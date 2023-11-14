from django.db import models

# Create your models here.
class Student(models.Model):
    Sno=models.CharField(max_length=9,primary_key=True)
    Sname=models.CharField(max_length=20)
    Ssex=models.CharField(max_length=2)
    Sage=models.IntegerField()
    Sdept=models.CharField(max_length=20)

class Course(models.Model):
    Cno=models.CharField(max_length=9,primary_key=True)
    Cname=models.CharField(max_length=20)
    Cpno=models.CharField(max_length=9)
    Ccredit=models.IntegerField()

class SC(models.Model):
    Sno=models.CharField(max_length=9)
    Cno=models.CharField(max_length=9)
    Grade=models.CharField(max_length=3)



