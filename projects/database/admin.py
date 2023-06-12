from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Registration
from .models import ProgramRegistration
from .models import AddApp


admin.site.site_header = 'Admin Tutorial Dashboard'


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'first_name','last_name', 'email','password','status', 'position', 'funded_by', 'annual_salary', 'annual_salary', 'is_admin', )


class ProgramRegistrationAdmin(admin.ModelAdmin):
    list_display = ('employee_id',)

admin.site.register(AddApp)
admin.site.register(Registration, RegistrationAdmin) 
admin.site.register(ProgramRegistration, ProgramRegistrationAdmin) 
from .models import CustomUser, InvestmentReport, Evaluation, Training, UserInvestment, UserEvaluation, UserTraining
from .forms import CustomUserForm


class CustomUserAdmin(admin.ModelAdmin):
    form = CustomUserForm
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(InvestmentReport)
admin.site.register(Evaluation)
admin.site.register(Training)
admin.site.register(UserInvestment)
admin.site.register(UserEvaluation)
admin.site.register(UserTraining)

# admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(InvestmentReport, InvestmentReportAdmin)
# admin.site.register(Evaluation, EvaluationAdmin)
# admin.site.register(Training, TrainingAdmin)
