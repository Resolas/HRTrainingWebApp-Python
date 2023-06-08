from django.db import models





class Registration(models.Model):
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

class ProgramRegistration(models.Model):
     employee_id = models.CharField(max_length=20, primary_key=True,)
     first_name = models.CharField(max_length=45, )
     last_name = models.CharField(max_length=45,)
     start_date = models.DateField()
     end_date = models.DateField()
     employee_status_choices = [
        ('active', 'Active'),
        ('inactive', 'Iaactive'),
        ('terminated', 'Terminated'),
    ]
     employee_status = models.CharField(max_length=20, choices=employee_status_choices)
     funded_by = models.TextField(max_length=45,)
     employee_email = models.EmailField(max_length=60,)




     def __str__(self):
        return self.employee_id

     def body_preview(self):
        return self.body[:50]


class AddApp(models.Model):
    application_date = models.CharField(max_length=100)
    employee_job_title = models.EmailField(max_length=100)
    length_of_service = models.CharField(max_length=100)
    training_course_name = models.CharField(max_length=100)
    training_course_provider = models.CharField(max_length=100)
    start_date = models.CharField(max_length=10)
    end_date = models.CharField(max_length=10)
    qualification = models.CharField(max_length=100)
    number_of_days = models.CharField(max_length=10)
    delivery_method = models.CharField(max_length=50)
    course_aims_and_objectives = models.CharField(max_length=500)
    expected_outcome = models.CharField(max_length=500)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    ballymun_job_centre_contribution = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.CharField(max_length=10)

    def __str__(self):
        return self.application_date
    
    class Meta:
        db_table = 'database_addApp'