from rest_framework import serializers
from .models import DoctorModel,PatientModel
from .models import AppointmentModel
from django.contrib.auth.models import User

class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','id','password')


class DoctorSerializer(serializers.ModelSerializer):
   doctor=CurrentUserSerializer()
   class Meta:
      model=DoctorModel
      fields=('id','speciality','title','doctor')

class PatientSerializer(serializers.ModelSerializer):
    patient=CurrentUserSerializer()
    class Meta:
        model=PatientModel
        fields=('id','patient')

class AppointmentSerializer(serializers.ModelSerializer):
    patient=PatientSerializer()
    doctor=DoctorSerializer()
    class Meta:
        model=AppointmentModel
        fields=('id','created_at','description','date','time','doctor','patient')