from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('employee', 'Employee'),
    )
    role_name = models.CharField(max_length=10, choices=ROLES, null=True)
    email = models.CharField(max_length=45, null=True, unique=True)
    first_name = models.CharField(max_length=45, null=True)
    last_name = models.CharField(max_length=45, null=True)
    position = models.CharField(max_length=45, null=True)
    funded_by = models.CharField(max_length=45, null=True)
    annual_salary = models.DecimalField(max_digits=10, decimal_places=0, null=True)

    def is_admin(self):
        return self.role_name == 'admin'
    
    def is_employee(self):
        return self.role_name == 'employee'
    
    class Meta:
        db_table = 'custom_user'

class InvestmentReport(models.Model):
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

    class Meta:
        db_table = 'investment_report'

class Evaluation(models.Model):
    employee_name = models.CharField(max_length=45)
    job_title = models.CharField(max_length=45)
    training_course = models.TextField()
    training_provider = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    no_of_days = models.IntegerField()
    certification = models.IntegerField()
    certification_reason = models.TextField()
    objective = models.TextField()
    topics = models.TextField()
    usefulness = models.TextField()
    three_important_points = models.TextField()
    topic_relevant = models.IntegerField()
    encouragement = models.IntegerField()
    material_helpfulness = models.IntegerField()
    objective_met = models.IntegerField()
    time_sufficient = models.IntegerField()
    expectation_met = models.IntegerField()

    class Meta:
        db_table = 'evaluation'

class Training(models.Model):
    employee_name = models.CharField(max_length=45)
    employee_position = models.CharField(max_length=45)
    length_of_service = models.CharField(max_length=45)
    application_date = models.DateField()
    programme_name = models.CharField(max_length=45)
    training_provider = models.CharField(max_length=45)
    start_date = models.DateField()
    end_date = models.DateField()
    no_of_days = models.IntegerField()
    delivery_method = models.IntegerField()
    programme_aims = models.TextField()
    programme_objectives = models.TextField()
    expected_outcome = models.TextField()

    bjc_contribution = models.TextField()
    emp_contribution = models.IntegerField()
    
    training_hours = models.IntegerField(null=True)
    application_status = models.IntegerField(null=True)
    current_status = models.IntegerField(null=True)

    total_cost = models.IntegerField(null=True)
    
    employee_contribution = models.TextField()
    employee_qualification = models.TextField()
    
    employee_signed = models.TextField()
    administrator_signed = models.TextField()

    class Meta:
        db_table = 'training'


    def __str__(self):
        return self.employee_name
    

#--------------- INTERMEDIARIES FOR FOREIGN KEYS ----------------------

class UserInvestment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    investment_report = models.ForeignKey(InvestmentReport, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_investment'

    def __str__(self):
        return f"{self.investment_report, self.user}"

class UserEvaluation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_evaluation'

class UserTraining(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_training'

    def __str__(self):
        return f"{self.user} - {self.training}"


