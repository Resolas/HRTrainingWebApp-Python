from django.db import models


class Employee(models.Model):
    employee_id = models.CharField(max_length=20, primary_key=True,)
    role_name = models.CharField(max_length=45, )
    first_name = models.CharField(max_length=45, )
    last_name = models.CharField(max_length=45,)
    email = models.CharField(max_length=40,)
    password = models.CharField(max_length=20,)
    status = models.CharField(max_length=8, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], )
    position = models.CharField(max_length=45,)
    funded_by = models.CharField(max_length=45,)
    annual_salary = models.DecimalField(max_digits=10, decimal_places=0,)
    is_admin = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')], )


    def __str__(self):
        return self.employee_id

    def body_preview(self):
        return self.body[:50]


