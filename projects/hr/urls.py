from django.contrib import admin
from django.urls import path
from database import views
from database.views import create_addApp
from database.views import staff_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff/', views.staff, name='staff.html'),
    path('', views.home, name='home'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('profile/', views.profile, name='profile'),
    path('profile/staff/', views.staff, name='staff'),
    path('profile/staff/addApp.html/', views.addApp, name='addApp'),
    path('saved/', views.saved, name='saved'),
    path('addApp/', views.addApp, name='addApp'),
    path('new-addApp/', create_addApp, name='create-addApp'),
    path('staff/', staff_view, name='staff'),
    path('success/', views.success_page, name='success-page'),
    path('profile/staff/evaluationpart1/evaluationpart2.html/', views.evaluationpart2, name='evaluationpart2'),


    #region Admin Section
    path('profile/admin/', views.admin, name='admin'),

    path('profile/admin/application', views.application, name='application'),

    path('profile/admin/pendingapplication/',views.pendingapplication, name='pendingapplication.html'),

    path('profile/admin/employeeregistration', views.employeeregistration, name='employeeregistration'),

    #path('profile/admin/evaluationpart1/',
    #     views.evaluationpart1, name='evaluationpart1'),
    #path('profile/admin/evaluationpart1/evaluationpart2/',
    #      views.evaluationpart2, name='evaluationpart2'),

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

    path('profile/staff/addApp/', views.addApp, name='addApp.html'),

    path('profile/staff/pendingapplication/',views.pendingapplication, name='pendingapplication.html'),

    path('profile/staff/evaluationpart1.html/', views.evaluationpart1, name='evaluationpart1'),
    path('profile/staff/evaluationpart1/evaluationpart2.html/', views.evaluationpart2, name='evaluationpart2'),

    #endregion
]
