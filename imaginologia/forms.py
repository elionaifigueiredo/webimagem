from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    
    class Meta:
        model = Paciente
        fields = ['nome','img']