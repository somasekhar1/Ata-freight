from django.db import models

class Employee_Createrole(models.Model):
    username=models.CharField(max_length=40)
    email=models.EmailField()
    password=models.CharField(max_length=20)

class Employees_leaves(models.Model):
    start_leave_date=models.DateField()
    end_leave_date=models.DateField()
    description=models.CharField(max_length=200)
    total_leaves=models.IntegerField()
    status=models.CharField(max_length=20,default='pending',null=True,blank=True)


class Manager_Createrole(models.Model):
    username=models.CharField(max_length=40)
    email=models.EmailField()
    password=models.CharField(max_length=20)
