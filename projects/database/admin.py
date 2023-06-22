from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, InvestmentReport, Evaluation, TrainingApplication, UserInvestment, UserEvaluation, UserTraining


class CustomUserAdmin(UserAdmin):
    # Specify the fields to display and edit in the admin panel
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Position',{'fields':('position',)}),
        ('Salary',{'fields':('gross_salary','daily_salary','half_salary')}),
    )

    # Specify the fields to display in the list view of users
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

    # Enable the search functionality for users
    search_fields = ('username', 'email', 'first_name', 'last_name')

    # Enable the add and change options for users
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    ordering = ('username',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

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


admin.site.register(CustomUser, CustomUserAdmin)
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