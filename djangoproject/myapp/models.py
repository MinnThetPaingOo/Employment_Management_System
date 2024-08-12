
from django.db import models

# Create your models here.
class Department(models.Model):
    DeptName = models.CharField(max_length=20)
    Supervisor = models.CharField(max_length=20)
    def __str__(self):
        return self.DeptName

class Employee(models.Model):
    DeptId = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="items")
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Rank = models.CharField(max_length=20)
    Salary = models.IntegerField()
    HireDate = models.DateField()

    def __str__(self):
        return self.Name
