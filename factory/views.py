# factory/views.py
from django.shortcuts import render

def index(request):
    context = {"clase": "index"}
    return render(request, 'demo/index.html', context)

def laboratorio(request):
    context = {"clase": "laboratorio"}
    return render(request, 'demo/laboratorio.html', context)

def home(request):
    return render(request, 'demo/index.html')

def contacto(request):
    return render(request, 'demo/contacto.html')

def pc_armados(request):
    return render(request, 'demo/pc_armados.html')

def pc_gamer(request):
    return render(request, 'demo/pc_gamer.html')

def workstations(request):
    return render(request, 'demo/workstations.html')

def home_office(request):
    return render(request, 'demo/home_office.html')

def carrito(request):
    return render(request, 'demo/carrito.html')

def registrarse(request):
    return render(request, 'demo/registrarse.html')

def transbank(request):
    return render(request, 'demo/transbank.html')
