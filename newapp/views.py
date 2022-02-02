import imp
from pyexpat import model
from django.shortcuts import render
from django.http import Http404
from .models import *

# Create your views here.

def pocetna(request):
  return render(request, 'pocetna.html')

def motori(request):
    try:
        lista_vbm = VanbrodskiMotori.objects.all()

        context = {'lista_vbm': lista_vbm}

    except motori.DoesNotExist:
        raise Http404('Motors do not exist')

    return render(request, 'motori.html', context=context)
  