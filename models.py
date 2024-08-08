from django.db import models

# Create your models here.
class Student(models.Model):
   # id  will be added by ORM 
   name = models.CharField(max_length=150) 
   email = models.CharField(max_length=150)
   contact = models.IntegerField()
   course = models.CharField(max_length=100)