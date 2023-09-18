from django.db import models

# Create your models here.
class Events(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
 
    class Meta:  
        db_table = "tblevents"

class TecCourse(models.Model):
    teachername = models.CharField(max_length=100, blank=False ,default="teacher")
    course = models.CharField(max_length=100, blank=False, default="new course")
    date = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return str(self.course)
    
    class Meta:  
        db_table = "courses"
        

class Student(models.Model):
    studentname = models.CharField(max_length=50, blank=False, default="student")
    course = models.ManyToManyField(TecCourse)
    date = models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return str(self.studentname)
    
    class Meta:  
        db_table = "students"
