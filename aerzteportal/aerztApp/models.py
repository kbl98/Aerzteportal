from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class DoctorModel(models.Model):
    speciality=models.CharField(max_length=15)
    title=models.CharField(max_length=15)
    doctor=models.ForeignKey(User,on_delete=models.CASCADE)


   

class PatientModel(models.Model):
    patient=models.ForeignKey(User,on_delete=models.CASCADE)

class AppointmentModel(models.Model):
    date=models.DateField
    time=models.TimeField
    description=models.CharField(max_length=200)
    created_at=models.DateTimeField(default=datetime.now)
    patient=models.ForeignKey(PatientModel,on_delete=models.CASCADE)
    doctor=models.ForeignKey(DoctorModel,on_delete=models.CASCADE)

    