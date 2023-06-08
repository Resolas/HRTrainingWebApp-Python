from django.contrib import admin
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