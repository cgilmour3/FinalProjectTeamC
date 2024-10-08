from django.shortcuts import render
from ProjectApp.models import Patient
from ProjectApp.models import Doctor
from ProjectApp.models import Specialist
from  django_tables2 import SingleTableView
from FinalProject.tables import PatienTable
# Create your views here.
def index(request):

    return render(request, 'index.html')

def patients(request):
    data = Patient.objects.all()
    context = {'Patients': data}
    return render(request, 'patients.html',context)

def doctors(request):
    data = Doctor.objects.all()
    context = {'Doctors': data}
    return render(request, 'doctors.html',context)

def help(request):
    
    return render(request, 'help.html')

def specialists(request):
    data = Specialist.objects.all()
    context = {'Specialists': data}
    return render(request, 'specialists.html',context)