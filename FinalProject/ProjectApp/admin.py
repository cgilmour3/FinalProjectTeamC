from django.contrib import admin
from ProjectApp.models import Patient
from ProjectApp.models import Doctor
from ProjectApp.models import Specialist
# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Specialist)