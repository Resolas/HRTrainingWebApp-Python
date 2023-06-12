from django.shortcuts import render, redirect
from django.db import connection
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect


from django.template import loader
from .models import InvestmentReport, Evaluation, Training, AddApp
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

def staff(request):
    return render(request, 'staff.html')

def addApp(request):
    return render(request, 'addApp.html')

def signout(request):
    logout(request)
    return redirect('/')

def saved(request):
    return render(request, 'saved.html')

def staff_view(request):
    return render(request, 'staff.html')  

def success_page(request):
    # Handle the success page logic
    return render(request, 'success.html')

def create_addApp(request):
    if request.method == 'POST':
        application_date = request.POST['application_date']
        employee_job_title = request.POST['employee_job_title']
        length_of_service = request.POST['length_of_service']
        training_course_name = request.POST['training_course_name']
        training_course_provider = request.POST['training_course_provider']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        qualification = request.POST['qualification']
        number_of_days = request.POST['number_of_days']
        delivery_method = request.POST['delivery_method']
        course_aims_and_objectives = request.POST['course_aims_and_objectives']
        expected_outcome = request.POST['expected_outcome']
        total_cost = request.POST['total_cost']
        ballymun_job_centre_contribution = request.POST['ballymun_job_centre_contribution']
        date = request.POST['date']
        new_app = AddApp(application_date=application_date,
            employee_job_title=employee_job_title,
            length_of_service=length_of_service,
            training_course_name=training_course_name,
            training_course_provider=training_course_provider,
            start_date=start_date,
            end_date=end_date,
            qualification=qualification,
            number_of_days=number_of_days,
            delivery_method=delivery_method,
            course_aims_and_objectives=course_aims_and_objectives,
            expected_outcome=expected_outcome,
            total_cost=total_cost,
            ballymun_job_centre_contribution=ballymun_job_centre_contribution,
            date=date
        )

        new_app.save()
        # Redirect to a success page or perform other actions
        return redirect('success-page')
    else:
        # Handle GET request or render the initial form
        return render(request, 'addApp.html')

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

#endregion



def display_Evaluation(request):
    data = Evaluation.objects.all()
    return render(request, 'evaluationpart1.html', {'data' : data})

def display_InvestmentReport(request):
    data = InvestmentReport.objects.all()  # Retrieve all instances of YourModel from the database
    return render(request, 'reports.html', {'data': data})

def display_Training(request):
    data = Training.objects.all()
    return render(request, 'reports.html', {'data': data})

# Staff Section Pages
def application(request):
    return render(request, 'application.html')
    
def pendingapplication(request):
    return render(request, 'pendingapplication.html')
