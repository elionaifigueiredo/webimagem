from django.contrib import admin

# Register your models here.

from imaginologia.models import Paciente

@admin.register(Paciente)
class AdminPaciente(admin.ModelAdmin):
    list_display = ['nome','img']

 


