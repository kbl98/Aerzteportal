from rest_framework import serializers
from .models import DoctorModel,PatientModel
from .models import AppointmentModel
from django.contrib.auth.models import User

class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','id')
    
    def create(self, validated_data):
        password = validated_data.get('password')
        user = User(**validated_data)
        user.set_password(password)  # Passwort hashen
        user.save()
        return user

class DoctorSerializer(serializers.ModelSerializer):
    #doctor=CurrentUserSerializer()
    class Meta:
      model=DoctorModel
      fields=('id','speciality','title','doctor')

    def create(self, validated_data):

        doctor_data = {
            'title': validated_data.get('title'),
            'speciality': validated_data.get('speciality'),
            'doctor': validated_data.get('doctor'),
        }
        new_doctor = DoctorModel.objects.create(**doctor_data)
        new_doctor.save()
        return new_doctor

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