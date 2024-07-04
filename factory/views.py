# factory/views.py
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
# from django.contrib.auth.decorators import login_required

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
    if request.method != "POST":
        context={"clase": "registrarse"}
        return render(request, 'demo/registrarse.html', context)
    else:
        nombre = request.POST["nombre"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.create_user(nombre, email, password)
        user.save()
        context={"clase": "registro", "mensaje":"Los datos fueron registrados"}
        return render(request, 'demo/registrarse.html', context)

def get_current_users():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
    # Query all logged in users based on id list
    return User.objects.filter(id__in=user_id_list)


def transbank(request):
    return render(request, 'demo/transbank.html')
