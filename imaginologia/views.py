from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from .forms import *


from imaginologia.models import Paciente

# Create your views here.

# Lista 
def index(request):
    pessoa = Paciente.objects.all()
    return render(request, "index.html", {'pessoa':pessoa})

# Adiciona 
def cadastro(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        form = PacienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('/raiox')
        else:
            form = PacienteForm
            return render(request, 'index.html')

# Imagens Detalhada
def display_img(request, id):
    try:
        paciente = Paciente.objects.filter(pk=id)
    except Paciente.DoesNotExist:
        raise Http404('Paciente Não existe!')
    return render(request, 'display_paciente_images.html', {'paciente': paciente})
