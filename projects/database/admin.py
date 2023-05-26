from django.contrib import admin
from django.contrib.auth.models import Group
from .models import TestTable
from .models import InvestmentReport

# Register your models here.


admin.site.site_header = 'Admin Tutorial Dashboard Hello'


# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ('role_name', 'first_name','last_name', 'email',
#                     'password','status', 'position', 'funded_by', 'annual_salary', 'annual_salary', 'is_admin', )

# admin.site.register(Employee, EmployeeAdmin)

class TestTableAdmin(admin.ModelAdmin):
    list_display = ('username_id','email','password')

admin.site.register(TestTable, TestTableAdmin)

class InvestmentReportAdmin(admin.ModelAdmin):
    list_display = ('investment_report_id','employee_name','scale',
                    'point_on_scale','funded_by','annual_salary','weekly_hours',
                    'gross_weekly','full_day_rate','half_day_rate','hourly_rate',)

admin.site.register(InvestmentReport, InvestmentReportAdmin)
