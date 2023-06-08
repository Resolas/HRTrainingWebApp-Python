from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Registration
from .models import ProgramRegistration


admin.site.site_header = 'Admin Tutorial Dashboard'


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'first_name','last_name', 'email','password','status', 'position', 'funded_by', 'annual_salary', 'annual_salary', 'is_admin', )


class ProgramRegistrationAdmin(admin.ModelAdmin):
    list_display = ('employee_id',)


admin.site.register(Registration, RegistrationAdmin) 
admin.site.register(ProgramRegistration, ProgramRegistrationAdmin) 