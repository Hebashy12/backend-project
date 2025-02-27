from django import forms
from .models import FilesPatients

class FilesPatientsForm(forms.ModelForm):
    class Meta:
        model = FilesPatients
        fields = ['files_name', 'patient_name']
