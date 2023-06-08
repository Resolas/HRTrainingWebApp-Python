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
from database.views import create_addApp
from database.views import staff_view


urlpatterns = [
    path('admin/', admin.site.urls),
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
    
    
     

]
