from django.db import models

# Create your models here.

#region example code
# class Employee(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
#endregion
    
class InvestmentReport(models.Model):
    investment_report_id = models.CharField(max_length=20, primary_key=True)
    employee_name = models.CharField(max_length=45)
    scale = models.CharField(max_length=45)
    point_on_scale = models.DecimalField(max_digits=10, decimal_places=0)
    funded_by = models.CharField(max_length=45)
    annual_salary = models.DecimalField(max_digits=10, decimal_places=0)
    weekly_hours = models.DecimalField(max_digits=10, decimal_places=0)
    gross_weekly = models.DecimalField(max_digits=10, decimal_places=0)
    full_day_rate = models.DecimalField(max_digits=10, decimal_places=0)
    half_day_rate = models.DecimalField(max_digits=10, decimal_places=0)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=0)
    admin_id = models.CharField(max_length=20)
    evaluation_id = models.CharField(max_length=20)
    employee_id = models.CharField(max_length=20)
    training_id = models.CharField(max_length=20)
    
    def __str__(self):
        return self.investment_report_id
    
class Evaluation(models.Model):
    evaluation_id = models.CharField(max_length=20, primary_key=True)
    employee_name = models.CharField(max_length=45)
    job_title = models.CharField(max_length=45)
    training_course = models.BinaryField()
    training_provider = models.BinaryField()
    start_date = models.DateField()
    end_date = models.DateField()
    no_of_days = models.IntegerField()
    certification = models.BooleanField()
    certification_reason = models.TextField()
    objective = models.TextField()
    topics = models.TextField()
    usefulness = models.TextField()
    three_important_points = models.TextField()
    topic_relevant = models.CharField(max_length=45)
    encouragement = models.CharField(max_length=45)
    material_helpfulness = models.CharField(max_length=45)
    objective_met = models.CharField(max_length=45)
    time_sufficient = models.CharField(max_length=45)
    expectation_met = models.CharField(max_length=45)
    admin_id = models.CharField(max_length=20)
    investment_report_id = models.CharField(max_length=20)
    employee_id = models.CharField(max_length=20)
    training_id = models.CharField(max_length=20)

    def __str__(self):
        return self.evaluation_id

    
class TestTable(models.Model):
    username_id = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    def __str__(self):
        return self.username_id


