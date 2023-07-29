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
        doctors=DoctorModel.objects.all
        serializer=DoctorSerializer(doctors)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request, format=None):
        data=request.data
        serializer = DoctorSerializer(data=data)
        if serializer.is_valid():
            newUser=User.objects.create(first_name=data['firstname'],last_name=data['lastname'],username=data['username'],password=data['password'])
    
            newUser.save()
            newDoctor=DoctorModel.objects.create(title=data['title'],speciality=data['speciality'],doctor=newUser)
            serializer=DoctorSerializer(newDoctor)
            newDoctor.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        

class Patients(APIView):
    def get(self, request, format=None):
        patients=PatientModel.objects.all
        serializer=PatientSerializer(patients)
        if serializer.is_valid:
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class Appointments(APIView):
    """
    On request User has to send the user id, to specify, which appointments can be shown
    """
    def get(self, request, format=None):
        id=request.data['id']
        if id is not None:
            appointments=AppointmentModel.objects.filter(Q(patient__id=id) | Q(doctor__id=id))
            serializer=AppointmentSerializer
            if serializer.is_valid:
                serializer.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)

            