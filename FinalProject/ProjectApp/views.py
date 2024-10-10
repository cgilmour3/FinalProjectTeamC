from django.shortcuts import render
from ProjectApp.models import Patient, Doctor, Specialist
# Create your views here.
def index(request):

    return render(request, 'index.html')

def patients(request):
    patient = Patient.objects.all()
    my_doct = {'mypatients': patient}
    return render(request, 'patients.html', context = my_doct)

def doctors(request):
    doctor = Doctor.objects.all()
    my_dict = {'mydoctors': doctor}
    return render(request, 'doctors.html', context=my_dict)