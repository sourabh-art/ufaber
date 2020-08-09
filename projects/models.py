from django.db import models
from datetime import date 

class Projects(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=500)
    startdate=models.DateField(auto_now=True)
    enddate=models.DateField(auto_now=True)
    duration=models.IntegerField(null=True)
    photo = models.ImageField(upload_to='static',null=True)

    def __str__(self):
        return self.name
    
class Task(models.Model):
    name=models.CharField(max_length=50)
    project=models.IntegerField(null=True)
    description=models.CharField(max_length=500)
    startdate=models.DateField(auto_now=True)
    enddate=models.DateField(auto_now=True)
    duration=models.IntegerField(null=True)
    asign_to=models.CharField(max_length=500,null=True)
    project_name=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name