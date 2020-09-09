"""intern_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.views.generic import TemplateView
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='crete_role.html')),
    path('employee/',views.employee,name='employee'),
    path('employee_login/',views.employee_login,name='employee_login'),
    path('login_details/',views.emp_login_details,name='login_details'),
    path('employe_register/',views.employe_register,name='employe_register'),
    path('employee_leave/',views.employee_leave,name='employee_leave'),
    path('employee_leave_status/',views.employee_leave_status,name='employee_leave_status'),
    path('manager/',views.manager,name='manager'),
    path('manager_register/',views.manager_register,name='manager_register'),
    path('manager_login/',views.manager_login,name='manager_login'),
    path('manager_login_details/',views.manager_login_details,name='manager_login_details'),
    path('aprove_status/',views.leave_aprove_status,name='leave_aprove_status'),
    path('employee_leave_success/',views.employee_leave_success,name='employee_leave_success'),
]
