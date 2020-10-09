
from django.db import models

class Student(models.Model):
    stid=models.IntegerField(primary_key=True,default=0)
    name=models.CharField(max_length=50)
    roll=models.IntegerField(default=0)
    add=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    