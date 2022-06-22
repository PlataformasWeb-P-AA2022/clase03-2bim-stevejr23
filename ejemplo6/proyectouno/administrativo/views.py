from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from administrativo.models import Matricula

# vista que permita presesentar las matriculas
# el nombre de la vista es index.

def index(request):
    matriculas =  Matricula.objects.all()
    diccionario = {'numero_matriculas': len(matriculas),'matriculas': matriculas}
    return render(request, 'index.html', diccionario)