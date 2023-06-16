from django import forms
from .models import CustomUser, TrainingApplication, Evaluation
from django.contrib.auth.forms import UserCreationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field

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
        fields = ['username', 'password1', 'password2','is_staff', 'email', 'first_name','last_name', 'position', 'funded_by',
                   'gross_salary', 'daily_salary', 'half_salary']

class TrainingCreationForm(forms.ModelForm):
    class Meta:
        model = TrainingApplication
        fields = ['employee_name','employee_position','length_of_service','application_date','programme_name',
                  'training_provider','start_date','end_date','no_of_days','no_of_hours','delivery_method','programme_aims',
                  'programme_objectives','expected_outcome','bjc_contribution','emp_contribution',
                  'employee_signed','administrator_signed']

class ChangePasswordForm(forms.Form):
    username = forms.ModelChoiceField(queryset=CustomUser.objects.all())
    new_password = forms.CharField(widget=forms.PasswordInput)


class EvaluationForm(forms.ModelForm):
    CHOICES = [
        (1, 'Strongly Disagree'),
        (2, 'Disagree'),
        (3, 'Neutral'),
        (4, 'Agree'),
        (5, 'Strongly Agree'),
    ]
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    topic_relevant = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    encouragement = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    material_helpfulness = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    objective_met = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    time_sufficient = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    expectation_met = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Evaluation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Field('employee'),
                Field('employee_name'),
                Field('job_title'),
                Field('training_course'),
                Field('training_provider'),
                Field('start_date'),
                Field('end_date'),
                Field('no_of_days'),
                Field('certification'),
                Field('certification_reason'),
                Field('objective'),
                Field('topics'),
                Field('usefulness'),
                Field('three_important_points'),
                Field('topic_relevant'),
                Field('encouragement'),
                Field('material_helpfulness'),
                Field('objective_met'),
                Field('time_sufficient'),
                Field('expectation_met'),
                css_class='form-check'
            ),
        )


