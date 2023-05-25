from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Employee


admin.site.site_header = 'Admin Tutorial Dashboard'


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'first_name','last_name', 'email','password','status', 'position', 'funded_by', 'annual_salary', 'annual_salary', 'is_admin', )



admin.site.register(Employee, EmployeeAdmin)
