import django_tables2 as tables
from ProjectApp.models import Patient

class PatienTable(tables.Table):
    class Meta:
        model = Patient
        template_name = "django_tables2/bootstrap.html"
        fields = ("first name", "Last name", "Age", "Gender", "Doctor")