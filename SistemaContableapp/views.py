from django.shortcuts import render
from .models import Project, Task, Solicitud, CollectionAccount
from .models import Task
from .models import Solicitud
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect   
from .forms import CreateNewTask, CollectionAccountForm
from django.conf import settings 
from django.template.loader import get_template  
from django.core.mail import get_connection, EmailMessage

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
      
"""  
def get_smtp_host(email):
    domain = email.split('@')[-1]
    if domain == 'gmail.com':
        return 'smtp.gmail.com'
    elif domain == 'yahoo.com':
        return 'smtp.mail.yahoo.com'
    elif domain == 'outlook.com' or domain == 'hotmail.com':
        return 'smtp.office365.com'

    else:
        return 'Error debido a la extension de correo electronico'  
"""  

def sendmailCollectionAccount(data):
    messageBody = get_template("sendCollectionAccountForm.html").render(data)

    email = EmailMessage("CollectionAccount Form", 
                         messageBody, settings.DEFAULT_FROM_EMAIL, 
                         to=["pinedapablo6718@gmail.com"]
                         )
    email.content_subtype = "html"
    return email.send()




def createCollectionAccountForm(request) :
    
    if request.method == 'POST':
        form = CollectionAccountForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit = False)
            form.save()
            
            
            data ={
                "remitente" : request.POST.get("remitente"),
                "nombre" : request.POST.get("nombre"),
                "identificacion" : request.POST.get("identificacion"),
                "sumadeValorEnLetras" : request.POST.get("sumadeValorEnLetras"),
                "sumadeValorEnNumeros" : request.POST.get("sumadeValorEnNumeros"),
                "concepto" : request.POST.get("concepto"),
                "ciudadYFecha" : request.POST.get("ciudadYFecha"),
                "direccion" : request.POST.get("direccion"),
                "nombreDelBanco" : request.POST.get("nombreDelBanco"),
                "tipoDeCuenta" : request.POST.get("tipoDeCuenta"),
                "NoDeCuenta" : request.POST.get("NoDeCuenta"),
                "cexNo" : request.POST.get("cexNo") 
            }
            
            sendmailCollectionAccount(data)
            
            
            
            
            return redirect("viewCollectionAccountForm")
    
    else :
        form = CollectionAccountForm()
    
    
    return render(request, "CollectionAccountForm.html", {"form" : form})
