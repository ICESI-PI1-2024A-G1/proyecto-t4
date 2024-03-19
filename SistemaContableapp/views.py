from django.shortcuts import render
from .models import Project, Task, CollectionAccount
from .models import Task

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect   
from .forms import CreateNewTask
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CreateNewTask, CollectionAccountForm
from django.conf import settings 
from django.template.loader import get_template  
from django.core.mail import get_connection, EmailMessage, EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.files import File
from django_renderpdf.views import PDFView

from django.core.files import File
import weasyprint

# Create your views here.

def index(request):
    title = "Hola Gabriela, ¡Bienvenida al Sistema Contable"
    return render(request,'index.html', {
        'title' : title 
    })


def login(request):
     return render(request, 'registration/login.html')

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
def solicitud(request):
      solicitud= Solicitud.objects.all()
      return render(request, 'solicitudes.html', {
        #'solicitudes' : solicitud
   })

def sendmailCollectionAccountToPdf(data):
    messageBody = get_template("sendCollectionAccountForm.html").render(data)

    # Generar PDF a partir del HTML
    pdf = weasyprint.HTML(string=messageBody).write_pdf()

    email = EmailMessage(
        "CollectionAccount Form",
        "Please find the CollectionAccount Form attached.",
        settings.DEFAULT_FROM_EMAIL,
        to=["pinedapablo6718@gmail.com"]
    )

    # Adjuntar el PDF generado
    email.attach('collection_account.pdf', pdf, 'application/pdf')

    return email.send()

def createCollectionAccountForm(request):
    if request.method == 'POST':
        form = CollectionAccountForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            data = {
                "remitente": request.POST.get("remitente"),
                "nombre": request.POST.get("nombre"),
                "identificacion": request.POST.get("identificacion"),
                "sumadeValorEnLetras": request.POST.get("sumadeValorEnLetras"),
                "sumadeValorEnNumeros": request.POST.get("sumadeValorEnNumeros"),
                "concepto": request.POST.get("concepto"),
                "ciudadYFecha": request.POST.get("ciudadYFecha"),
                "direccion": request.POST.get("direccion"),
                "nombreDelBanco": request.POST.get("nombreDelBanco"),
                "tipoDeCuenta": request.POST.get("tipoDeCuenta"),
                "NoDeCuenta": request.POST.get("NoDeCuenta"),
                "cexNo": request.POST.get("cexNo")
            }
            sendmailCollectionAccountToPdf(data)
            return redirect("viewCollectionAccountForm")
    else:
        form = CollectionAccountForm()
    return render(request, "CollectionAccountForm.html", {"form": form})
