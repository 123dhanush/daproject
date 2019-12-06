from django.db import models

# Create your models here.
class teacher(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    
class student(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    courses=models.CharField(max_length=50,default="NA")

class filedb(models.Model):
    filename=models.CharField(max_length=50)
    fileurl=models.CharField(max_length=500)
    fcount=models.IntegerField(default=0)
    courseid=models.CharField(max_length=50)
    filecontent=models.FileField()

class studentstats(models.Model):
    susername=models.CharField(max_length=50)
    filename=models.CharField(max_length=50)
    fcount=models.IntegerField(default=0)
    courseid=models.CharField(max_length=50)
    

class course(models.Model):
    courseid=models.CharField(max_length=50,primary_key=True)
    coursename=models.CharField(max_length=50)
    credits1=models.CharField(max_length=10)
    coordinator=models.CharField(max_length=50)
    

