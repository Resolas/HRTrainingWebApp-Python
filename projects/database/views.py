from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from django.template import loader
from django.contrib.auth.decorators import user_passes_test, login_required
#from database.views import get_404
from .models import InvestmentReport, Evaluation, TrainingApplication, CustomUser, UserTraining
from .forms import CustomUserCreationForm, ChangePasswordForm, TrainingCreationForm, EvaluationForm

# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
    

#-------------------------
@login_required
@user_passes_test(lambda user: user.is_staff)
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Registration successful')
            return redirect('/profile/admin')
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'employeeregistration.html', {'form': form})


def success_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return render(request, 'success.html')
        else:
            # If the form is not valid, re-render the form page with the errors
            return render(request, 'employeeregistration.html', {'form': form})
    else:
        # If the request method is not POST, render the form page again
        form = CustomUserCreationForm()
        return render(request, 'employeeregistration.html', {'form': form})

# def changepassword(request):
#     form = ChangePasswordForm()
#     return render(request, 'changepassword.html', {'form': form})

@login_required
@user_passes_test(lambda user: user.is_staff)
def changepassword(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            new_password = form.cleaned_data['new_password']
            user.set_password(new_password)
            user.save()
            #messages.success(request, 'Password changed successfully.')
            return redirect('/profile/admin')
    else:
        form = ChangePasswordForm()
    return render(request, 'changepassword.html', {'form': form})

@login_required
def applyfortraining(request):
    if request.method == 'POST':
        form = TrainingCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Application successful')
            return redirect('/profile/staff')   # 'staff' will be changed to 'employee'
        else:
            print(form.errors)
    else:
        form = TrainingCreationForm()
    return render(request, 'application.html', {'form': form})

#--------------------------------


def home(request):
    return render(request, 'home.html')

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff == 1:
                return redirect('/profile/admin')  # Redirect to admin page
            else:
                return redirect('/profile/staff')  # Redirect to staff page
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    
#def loadreport(request):

#region admin section



def profile(request):
    render(request, 'evaluationpart1.html')
    return render(request, 'profile.html')

def signout(request):
    logout(request)
    return redirect('/')

def training_evaluations_list(request):
    return render(request, 'training_evaluations_list.html')

def evaluationpart1(request):
    return render(request, 'evaluationpart1.html')

def evaluationpart2(request):
    return render(request, 'evaluationpart2.html')

def admin(request):
    return render(request, 'admin.html')

def staff(request):
    return render(request, 'staff.html')

def employeepersonaldetailspart1(request):
    return render(request, 'employeepersonaldetailspart1.html')
def employeepersonaldetailspart2(request):
    return render(request, 'employeepersonaldetails2.html')

def trainingcourseoverview(request):
    return render(request, 'trainingcourseoverview.html')
def trainingcoursedetails(request):
    return render(request, 'trainingcoursedetails.html')

def employeeregistration(request):
    return render(request, 'employeeregistration.html')
def programregistration(request):
    return render(request, 'programregistration.html')

def reports(request):
    return render(request, 'reports.html')

#endregion

#region other functions

# def get_Page_Name(request):
#     currentPage = loader.get_template(request.path).name
#     context = {'currentPage': currentPage}
#     return render(request, 'my_template.html', context)

def get_404(request, exception):
    return render(request, 'get_404.html', status=404)

#endregion



def display_Evaluation(request):
    data = Evaluation.objects.all()
    return render(request, 'training_evaluations_list.html', {'data' : data})

def display_InvestmentReport(request):
    data = InvestmentReport.objects.all()  # Retrieve all instances of YourModel from the database
    return render(request, 'reports.html', {'data': data})

def display_Training(request):
    data = TrainingApplication.objects.all()
    return render(request, 'reports.html', {'data': data})

# Staff Section Pages
# def application(request):
#     return render(request, 'application.html')

@login_required
def pendingapplication(request):
    return render(request, 'pendingapplication.html')

@login_required
def create_evaluation(request):
    evaluations = Evaluation.objects.all()
    if request.method == 'POST':
        form = EvaluationForm(request.POST)
        if form.is_valid():
            form.save()
            # Handle successful form submission
    else:
        form = EvaluationForm()
    context = {'form': form, 'evaluations':evaluations}
    return render(request, 'create_evaluation.html', context)





#region Training Course Application Functions

from django.contrib.auth.decorators import login_required


from django.shortcuts import redirect

@login_required
def application(request):
    if request.method == 'POST':
        form = TrainingCreationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.employee_name = request.user.get_full_name()  # Set the employee name as the full name of the logged-in user
            application.save()
            form.save_m2m()  # Save the many-to-many relationships if any
            application.users.add(request.user)  # Associate the logged-in user with the application
            return redirect('employee_training_applications_list')  # Redirect to the list view after successful submission
    else:
        form = TrainingCreationForm()
    context = {'form': form}
    return render(request, 'application.html', context)


#endregion


#region Training Application
@login_required
def edit_training_application(request, application_id):
    '''
    View to edit a course application made by the user.
    '''
    user_training = get_object_or_404(UserTraining, training_id=application_id, user=request.user)
    application = user_training.training

    form = TrainingCreationForm(request.POST or None, instance=application)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('course_application_list')

    context = {'application': application, 'form': form}
    return render(request, 'edit_training_application.html', context)

@login_required
def delete_training_application(request, app_id):
    application = get_object_or_404(TrainingApplication, id=app_id)
    if request.method == 'POST':
        application.delete()
        return redirect('course_application_list')
    
    return render(request, 'delete_application.html', {'application': application})

@login_required
@user_passes_test(lambda user: user.is_staff)
def approve_application(request, app_id):
    application = get_object_or_404(TrainingApplication, id=app_id)
    application.application_status = 'approved'
    application.save()
    return redirect('training_application_details', app_id=app_id)

@login_required
@user_passes_test(lambda user: user.is_staff)
def deny_application(request, app_id):
    application = get_object_or_404(TrainingApplication, id=app_id)
    if request.method == 'POST':
        reason = request.POST.get('reason', '')
        application.application_status = 'denied'
        application.reason_for_denial = reason
        application.save()
    return redirect('training_application_details', app_id=app_id)

@login_required
@user_passes_test(lambda user: user.is_staff)
def training_applications_list(request):    # Admin View
    applications = TrainingApplication.objects.all()
    total_applications = applications.count()
    return render(request, 'training_applications_list.html', {'applications': applications, "total_applications": total_applications})

#Function to show the details of the pending applications
#This view handles the details of applications which are viewable for the admin
@login_required
@user_passes_test(lambda user: user.is_staff)
def training_application_details(request, app_id):
    application = get_object_or_404(TrainingApplication, id=app_id)
    return render(request, 'training_application_details.html', {'application': application})



#endregion

#region Employee Training Applications
#Function to create a list view of pending applications
#This view handles the list of applciations for the admin to view
@login_required
def employee_training_applications_list(request):
    applications = UserTraining.objects.filter(user=request.user).select_related('training')
    total_applications = applications.count()
    return render(request, 'employee_training_applications_list.html', {'applications': applications, "total_applications": total_applications})

#Function to show the details of the pending applications
#This view handles the details of applications which are viewable for the admin
@login_required
def employee_training_application_details(request, id):
    application = get_object_or_404(TrainingApplication, id=id)
    return render(request, 'employee_training_application_details.html', {"application":application})

@login_required
def evaluation_applications_list(request):
    evaluations = Evaluation.objects.all()
    total_evaluations = evaluations.count()
    return render(request, 'training_evaluations_list.html', {'evaluations': evaluations, "total_evaluations": total_evaluations})

#endregion

#region Evaluation Form

def completed_evaluation(request, evaluation_id):
    evaluation = get_object_or_404(Evaluation, id=evaluation_id)

    if request.method == 'POST':
        form = EvaluationForm(request.POST, instance=evaluation)
        if form.is_valid():
            form.save()
            # Handle successful form submission
            return redirect('staff.html')  # Redirect to the evaluation list page
    else:
        form = EvaluationForm(instance=evaluation)
        
    context = {'form': form}
    return render(request, 'completed_evaluation.html', context)


#endregion
