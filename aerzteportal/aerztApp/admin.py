from django.contrib import admin
from .models import AppointmentModel,PatientModel
from .models import DoctorModel

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display=['id','created_at','date','time','description','doctor','patient',]

class PatientAdmin(admin.ModelAdmin):
    list_display=['patient','id']

class DoctorAdmin(admin.ModelAdmin):
    list_display=['doctor','speciality','title','id']

admin.site.register(AppointmentModel,AppointmentAdmin)
admin.site.register(PatientModel,PatientAdmin)
admin.site.register(DoctorModel,DoctorAdmin)
