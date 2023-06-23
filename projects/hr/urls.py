"""
URL configuration for hr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from database import views

app_name = 'database'

urlpatterns = [
    #region General Urls

    path('admin/', admin.site.urls),
    path('staff/', views.staff, name='staff'),
    path('', views.home, name='home'),
    path('signin/',views.signin, name='signin'),
    path('signup/',views.signup, name='signup'),
    path('signout/',views.signout, name='signout'),
    path('profile/',views.profile, name='profile'),
        path('success.html', views.success_view, name='success'),

#endregion

    #region Admin Section
    path('profile/admin/', views.admin, name='admin'),

    path('profile/admin/changepassword', views.changepassword, name='changepassword'),

    # path('profile/admin/application', views.application, name='application'),

    path('profile/admin/training_applications_list/',views.training_applications_list, name='training_applications_list'),

    path('profile/admin/employeeregistration', views.register_view, name='employeeregistration'),

    path('profile/admin/course_evaluation_list/',views.course_evaluation_list, name='training_evaluation_list'),
    path('profile/admin/course_evaluation_list/<int:app_id>/',views.course_evaluation_details, name='evaluationpart2'),

    path('profile/admin/employeepersonaldetailspart1/', views.employeepersonaldetailspart1,
        name='employeepersonaldetailspart1'),
    path('profile/admin/employeepersonaldetails2/', views.employeepersonaldetailspart1,
        name='employeepersonaldetails2'),

    path('profile/admin/trainingcourseoverview/', views.trainingcourseoverview, name='trainingcourseoverview.html'),
    path('profile/admin/trainingcourseoverview/trainingcoursedetails/', views.trainingcoursedetails, name='trainingcoursedetails.html'),

    #path('profile/admin/testtable/', views.test_table,name='testtable'),
    #path('profile/admin/reports/', views.test_table2,name='reports'),
    path('profile/admin/reports/', views.display_InvestmentReport, name='reports'),

    path('profile/admin/create_evaluation/<int:pk>/',
         views.create_evaluation, name='create_evaluation.html'),

    

    #endregion

    #region Staff Section

    path('profile/staff/', views.staff, name='staff.html'),
    
    path('profile/staff/application/', views.applyfortraining, name='application.html'),

    path('profile/staff/pendingapplication/',views.pendingapplication, name='pendingapplication.html'),

    # path('profile/staff/evaluationpart1/',
    #      views.evaluationpart1, name='evaluationpart1'),
    # path('profile/staff/evaluationpart1/evaluationpart2/',
    #       views.evaluationpart2, name='evaluationpart2'),

    path('profile/staff/completed_evaluation/',
        views.completed_evaluation, name='completed_evaluation'),

    path('profile/staff/create_evaluation/<int:pk>/', views.create_evaluation, name='create_evaluation'),

    #endregion

    #region Training Course Application Depracated URLS

    path('profile/staff/course_application/',views.application, name='course_application'),

    # #URL path for pending applicaitons page
    # path('profile/staff/training_applications_list',views.training_applications_list, name='training_applications_list'),
    # approve employee application
    # path('approve/<int:app_id>/', views.approve_application, name='approve_application'),
    # #Deny Path 
    # path('deny/<int:app_id>/', views.deny_application, name='deny_application'),
    # # #URL path for details of each application
    # path('training_application_details/<int:app_id>/',views.training_application_details,
    #       name='training_application_details'),
    # #URL path for pending applicaitons page
     path('profile/staff/course_application_list',views.employee_training_applications_list,
           name='course_application_list'),
    # #URL path for details of each application
    # path('employee_training_application_details/<int:id>/',views.employee_training_application_details,
        #   name='employee_training_application_details'),

    #endregion

    #region Training/Course Application URLs

    # #URL path for pending applicaitons page
    # path('profile/staff/training_applications_list',views.training_applications_list, name='training_applications_list'),
    # approve employee application
    path('approve/<int:app_id>/', views.approve_application, name='approve_application'),
    #Deny Path for denying application
    path('deny/<int:app_id>/', views.deny_application, name='deny_application'),
    #URL path for details of each application
    path('training_application_details/<int:app_id>/',views.training_application_details, name='training_application_details'),
    #URL path for pending applications page
    path('profile/staff/employee_training_applications_list',views.employee_training_applications_list, name='employee_training_applications_list'),
    #URL path for details of each application
    path('employee_training_application_details/<int:id>/',views.employee_training_application_details, name='employee_training_application_details'),
    #URL Path for editing training application
    path('edit/<int:application_id>/', views.edit_training_application, name='edit_training_application'),
    #URL Path to delete application
    path('delete/<int:app_id>/', views.delete_training_application, name='delete_application'),

    #endregion


    #region Evaluation Urls

    path('profile/admin/course_evaluation_list/',views.course_evaluation_list, name='course_evaluation_list'),
    path('profile/admin/course_evaluation_details/<int:app_id>/',views.course_evaluation_details, name='course_evaluation_details'),

    path('profile/staff/employee_course_evaluation_list/',views.employee_course_evaluation_list, name='employee_course_evaluation_list'),
    path('profile/staff/employee_course_evaluation_details/<int:app_id>/',views.employee_course_evaluation_details, name='employee_course_evaluation_details'),

    #endregion


]

handler404 = 'database.views.get_404'
