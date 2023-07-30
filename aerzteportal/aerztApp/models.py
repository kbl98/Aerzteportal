from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class DoctorModel(models.Model):
    speciality=models.CharField(max_length=15)
    title=models.CharField(max_length=15)
    doctor=models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.doctor.username if self.doctor else 'No doctor assigned'

   
class PatientModel(models.Model):
    patient=models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.patient.username if self.patient else 'No patient assigned'
    
class AppointmentModel(models.Model):
    date=models.DateField(default=date.today)
    time=models.TimeField(default=datetime.now)
    description=models.CharField(max_length=200)
    created_at=models.DateTimeField(default=datetime.now)
    patient=models.ForeignKey(PatientModel,on_delete=models.CASCADE,blank=True, null=True,)
    doctor=models.ForeignKey(DoctorModel,on_delete=models.CASCADE,blank=True, null=True,)

    