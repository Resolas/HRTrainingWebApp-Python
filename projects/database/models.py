
# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models

class Employee(AbstractUser):
    employee_id = models.CharField(primary_key=True, max_length=45)
    role_name = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    position = models.CharField(max_length=45)
    funded_by = models.CharField(max_length=45)
    annual_salary = models.DecimalField(max_digits=10, decimal_places=0)

    # Additional fields specific to employees
    department = models.CharField(max_length=45)
    hire_date = models.DateField()
    # Add other fields as per your requirements


    
    class Meta:
        db_table = 'employee'   
