from django.shortcuts import render
from .models import Project
from .models import Task
from .models import Solicitud
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect   
from .forms import CreateNewTask
# Create your views here.

#def hello (request, username):
    #print(username)
    #return HttpResponse("<h2>Hello %s </h2>" % username)

#---------------Tutorial---------------------------    

def index(request):
    title = "Hola Gabriela, ¡Bienvenida al Sistema Contable"
    return render(request,'index.html', {
        'title' : title 
    })

def solicitud(request):
      solicitud= Solicitud.objects.all()
      return render(request, 'solicitudes.html', {
        #'solicitudes' : solicitud
   })
    