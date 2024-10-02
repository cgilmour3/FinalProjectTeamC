from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'index.html')

def patients(request):
    
    return render(request, 'patients.html')

def doctors(request):

    return render(request, 'doctors.html')