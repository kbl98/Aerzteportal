from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from .models import AppointmentModel,DoctorModel
from .models import PatientModel
from .serializers import DoctorSerializer,PatientSerializer
from .serializers import CurrentUserSerializer,AppointmentSerializer
from rest_framework import status
from django.db.models import Q




# Create your views here.
class Doctors(APIView):
    def get(self, request, format=None):
        doctors=DoctorModel.objects.all()
        serializer=DoctorSerializer(doctors,many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
       
    def post(self, request, format=None):
        """
        Create new Doctor-User with passing firstname,lastname,password,username,title,speciality in JSON-request
        """
        data=request.data
        newUser=User.objects.create(first_name=data.get('firstname'),last_name=data.get('lastname'),username=data.get('username'),password=data.get('password'))
        userSerializer=CurrentUserSerializer(newUser)
        
        newUser.save()
       
        newDoctor=DoctorModel.objects.create(title=data.get('title'),speciality=data.get('speciality'))
        newDoctor.doctor=newUser
        newDoctor.save()
        serializer=DoctorSerializer(newDoctor)
        if serializer.is_valid:   
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class DoctorDetail(APIView):
    """
    For delete pk of doctor-object has to be send in url
    """
    def delete(self,request,pk,format=None):
        try:
            deleteDoctor=DoctorModel.objects.filter(pk=pk)  
            deleteDoctor.delete() 
            return Response({"status": "success", "message": "Arzt erfolgreich gelöscht."},status=status.HTTP_204_NO_CONTENT) 
        except DoctorModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)



class Patients(APIView):
    def get(self, request, format=None):
        patients=PatientModel.objects.all()
        serializer=PatientSerializer(patients,many=True)
        
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        
    def post(self, request, format=None):
        """
        Create new Patient-User with passing firstname,lastname,password,username in JSON-request
        """
        data=request.data
        newUser=User.objects.create(first_name=data.get('firstname'),last_name=data.get('lastname'),username=data.get('username'),password=data.get('password'))
        userSerializer=CurrentUserSerializer(newUser)
        
        newUser.save()
       
        newPatient=PatientModel.objects.create()
        newPatient.patient=newUser
        newPatient.save()
        serializer=PatientSerializer(newPatient)
        if serializer.is_valid:   
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class PatientDetail(APIView):
    def delete(self,request,pk,format=None):
        """
        Delete one Patient with sending id at request 'patients/id/'
        """
        try:
            deletePatient=PatientModel.objects.filter(pk=pk)  
            deletePatient.delete() 
            return Response({"status": "success", "message": "Patient erfolgreich gelöscht."},status=status.HTTP_204_NO_CONTENT) 
        except DoctorModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class Appointments(APIView):
    """
    On get-request User has to send the user id, to specify, which appointments can be shown
    For post the doctorID and patientID, and all necessary info about appointment (date yyyy-mm-dd,time hh:mm,description) have to be send
    
    """
    def get(self, request, format=None):
        id=request.data.get('id')
        selected_user = User.objects.filter(id=id).first()
        
        if selected_user:
            appointments=AppointmentModel.objects.filter(Q(patient__patient=selected_user) | Q(doctor__doctor=selected_user))
            print (appointments)
            serializer=AppointmentSerializer(appointments,many=True)
            
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
       
    def post(self, request,  *args, **kwargs):
        data=request.data
        appointment=AppointmentModel.objects.create(date=data['date'],time=data['time'],description=data['description'])
        doctor=DoctorModel.objects.get(id=data.get('doctorID'))
        patient=PatientModel.objects.get(id=data.get('patientID'))
        appointment.doctor=doctor
        appointment.patient=patient
        appointment.save()
        serializer=AppointmentSerializer(appointment)
        if serializer.is_valid:   
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class AppointmentDetail(APIView):
    """
    delete appointment on sending pk of appointment that has to be deleted
    """
    def delete(self,request,pk,format=None):
        try:
            deleteAppointment=AppointmentModel.objects.get(pk=pk) 
            deleteAppointment.delete()
            return Response({"status": "success", "message": "Appointment erfolgreich gelöscht."},status=status.HTTP_204_NO_CONTENT) 
        except AppointmentModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND) 
