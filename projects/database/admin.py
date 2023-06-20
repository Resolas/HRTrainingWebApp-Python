from django.contrib import admin
from .models import CustomUser, InvestmentReport, Evaluation, TrainingApplication, UserInvestment, UserEvaluation, UserTraining


class ReadOnlyModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Disable the add button
        return False

    def has_change_permission(self, request, obj=None):
        # Disable the edit button
        return False

    def has_delete_permission(self, request, obj=None):
        # Disable the delete button
        return False

    def get_readonly_fields(self, request, obj=None):
        # Make all fields read-only
        return [field.name for field in self.model._meta.fields]


admin.site.register(CustomUser, ReadOnlyModelAdmin)
admin.site.register(InvestmentReport, ReadOnlyModelAdmin)
admin.site.register(Evaluation, ReadOnlyModelAdmin)
admin.site.register(TrainingApplication, ReadOnlyModelAdmin)
admin.site.register(UserInvestment, ReadOnlyModelAdmin)
admin.site.register(UserEvaluation, ReadOnlyModelAdmin)
admin.site.register(UserTraining, ReadOnlyModelAdmin)

# admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(InvestmentReport, InvestmentReportAdmin)
# admin.site.register(Evaluation, EvaluationAdmin)
# admin.site.register(Training, TrainingAdmin)