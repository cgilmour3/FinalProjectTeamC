from django.db import models

# Create your models here.
class Patient(models.Model):
    GENDER_OPTIONS = [
        ('Male','male'), ('Female','female'), ('Other','other')
    ]
    patient_fname = models.CharField(max_length=40)
    patient_lname = models.CharField(max_length=50)
    patient_age = models.IntegerField()
    patient_gender = models.CharField(max_length=20, choices=GENDER_OPTIONS)
    patient_doctor = models.CharField(max_length=30)

class Doctor(models.Model):
    doctor_fname = models.CharField(max_length=40)
    doctor_lname = models.CharField(max_length=50)
    doctor_specialty = models.CharField(max_length=50)

class Specialist(models.Model):
    specialist_fname = models.CharField(max_length=40)
    specialist_lname = models.CharField(max_length=50)
    specialist_specialty = models.CharField(max_length=50)