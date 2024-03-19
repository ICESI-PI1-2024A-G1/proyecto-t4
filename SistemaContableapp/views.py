from django.shortcuts import render
from .models import Project
from .models import Task

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect   
from .forms import CreateNewTask
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

#def hello (request, username):
    #print(username)
    #return HttpResponse("<h2>Hello %s </h2>" % username)

#---------------Tutorial---------------------------    




def login(request):
     return render(request, 'registration/login.html')

def index(request):
    title = "Hola Gabriela, ¡Bienvenida al Sistema Contable"
    return render(request,'index.html', {
        'title' : title 
    })

#def login(request):
    #if request.method == 'POST':
       # email = request.POST.get('email')
       # password = request.POST.get('password')

        #user = authenticate(request, email=email, password=password)
       # if user is not None:
            #login(request, user)
            #return redirect('') # ruta del tablero 
       # else:
           # messages.error(request, 'Correo inválido. Inténtalo de nuevo.')

    #return render(request, 'registration/login.html')
