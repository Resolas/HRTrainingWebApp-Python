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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff/', views.staff, name='staff'),
    path('', views.home, name='home'),
    path('signin/',views.signin, name='signin'),
    path('signup/',views.signup, name='signup'),
    path('signout/',views.signout, name='signout'),
    path('profile/',views.profile, name='profile'),
    


    #region Admin Section
    path('profile/admin/', views.admin, name='admin'),

    path('profile/admin/changepassword', views.changepassword, name='changepassword'),

    path('profile/admin/application', views.application, name='application'),

    path('profile/admin/pendingapplication/',views.pendingapplication, name='pendingapplication.html'),

    path('profile/admin/employeeregistration', views.register_view, name='employeeregistration'),

    path('profile/admin/evaluationpart1/',
         views.evaluationpart1, name='evaluationpart1'),
    path('profile/admin/evaluationpart1/evaluationpart2/',
          views.evaluationpart2, name='evaluationpart2'),

    path('profile/admin/employeepersonaldetailspart1/', views.employeepersonaldetailspart1,
        name='employeepersonaldetailspart1'),
    path('profile/admin/employeepersonaldetails2/', views.employeepersonaldetailspart1,
        name='employeepersonaldetails2'),

    path('profile/admin/trainingcourseoverview/', views.trainingcourseoverview, name='trainingcourseoverview.html'),
    path('profile/admin/trainingcourseoverview/trainingcoursedetails/', views.trainingcoursedetails, name='trainingcoursedetails.html'),

    #path('profile/admin/testtable/', views.test_table,name='testtable'),
    #path('profile/admin/reports/', views.test_table2,name='reports'),
    path('profile/admin/reports/', views.display_InvestmentReport, name='reports'),

    

    #endregion

    #region Staff Section

    path('profile/staff/', views.staff, name='staff.html'),
    
    path('profile/staff/application/', views.applyfortraining, name='application.html'),

    path('profile/staff/pendingapplication/',views.pendingapplication, name='pendingapplication.html'),

    path('profile/staff/evaluationpart1/',
         views.evaluationpart1, name='evaluationpart1'),
    path('profile/staff/evaluationpart1/evaluationpart2/',
          views.evaluationpart2, name='evaluationpart2'),

    #endregion
]
