from rest_framework import serializers
from .models import DoctorModel,PatientModel
from .models import AppointmentModel
from django.contrib.auth.models import User

class CurrentUserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','id')


class DoctorSerializer(serializers.Serializer):
   doctor=CurrentUserSerializer
   class Meta:
      model=DoctorModel
      fields=('id','speciality','title','last_name','first_name')

class PatientSerializer(serializers.Serializer):
    patient=CurrentUserSerializer
    class Meta:
        fields=('id','last_name','first_name')

class AppointmentSerializer(serializers.Serializer):
    patient=CurrentUserSerializer
    doctor=CurrentUserSerializer
    class Meta:
        model=AppointmentModel