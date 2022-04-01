from unittest import loader
from django.shortcuts import render
from familia.models import *
# Create your views here.


def FamiliaView(request):
    familia = Familia.objects.all()
    return render(request,'familia/inicio.html', {"familia": familia, "title": "Familia", "page": "Familia"})
