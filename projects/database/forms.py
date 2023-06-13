from django import forms
from .models import CustomUser, Training
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        exclude = (
            'employee_id',
            'investment_report',
            'training',
            'evaluation',
            'groups',
            'user_permissions'
        )
class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)






class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'email', 'first_name','last_name', 'position', 'funded_by', 'annual_salary']

class TrainingCreationForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['employee_name','employee_position','length_of_service','application_date','programme_name',
                  'training_provider','start_date','end_date','no_of_days','delivery_method','programme_aims',
                  'programme_objectives','expected_outcome','bjc_contribution','emp_contribution',
                  'employee_signed','administrator_signed']

class ChangePasswordForm(forms.Form):
    username = forms.ModelChoiceField(queryset=CustomUser.objects.all())
    new_password = forms.CharField(widget=forms.PasswordInput)


