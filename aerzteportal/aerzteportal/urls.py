"""aerzteportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from aerztApp.views import Doctors,Patients
from aerztApp.views import Appointments,DoctorDetail
from aerztApp.views import PatientDetail,AppointmentDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctors/',Doctors.as_view()),
    path('patients/',Patients.as_view()),
    path('doctors/<int:pk>/', DoctorDetail.as_view()),
    path('patients/<int:pk>/', PatientDetail.as_view()),
    path('appointments/',Appointments.as_view()),
    path('appointments/<int:pk>/', AppointmentDetail.as_view()),
]
