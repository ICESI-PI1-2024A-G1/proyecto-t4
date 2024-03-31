from django.shortcuts import render
from .models import  *
from django.db.models import Q  
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect   
from .forms import CreateNewTask
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import *
from django.conf import settings 
from django.template.loader import get_template  
from django.core.mail import get_connection, EmailMessage
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMessage
import weasyprint
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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

def sendmailChargeAccountToPdf(data):
    messageBody = get_template("sendChargeAccountForm.html").render(data)

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

def createChargeAccountForm(request):
    if request.method == 'POST':
        form = ChargeAccountForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            data = { "name" : request.POST.get('name'),
                "identification" : request.POST.get('identification'),
                "concept" : request.POST.get('concept'),
                "value"  : request.POST.get('value'),
                "retention_392_401"  : request.POST.get('retention_392_401'),
                "retention_383" : request.POST.get('retention_383'),
                "declarant"  : request.POST.get('declarant'),
                "colombian_resident"  : request.POST.get('colombian_resident'),
                "city"  : request.POST.get('city'),
                "date"  : request.POST.get('date'),
                "cex"  : request.POST.get('cex'),
                "bank"  : request.POST.get('bank'),
                "type"  : request.POST.get('type'),
                "account_number"  : request.POST.get('account_number')
            }
            sendmailChargeAccountToPdf(data)
            return redirect("viewChargeAccountForm")
    else:
        form = ChargeAccountForm()
    return render(request, "chargeAccountForm.html", {"form": form})

def summaryOneStopShopView(request):


    # Obtener todos los objetos de Following
    queryset = Following.objects.all()
    
    # Obtener parámetros de búsqueda y filtrado
    query = request.GET.get('q')
    estado = request.GET.get('estado')
    tipo = request.GET.get('tipo')
    ordenar_por = request.GET.get("ordenar_por", None)
    fecha_creacion_inicio = request.GET.get('fecha_creacion_inicio')
    fecha_creacion_fin = request.GET.get('fecha_creacion_fin')
    fecha_cierre_inicio = request.GET.get('fecha_cierre_inicio')
    fecha_cierre_fin = request.GET.get('fecha_cierre_fin')
    
    # Aplicar filtros según los parámetros recibidos
    if query:
        queryset = queryset.filter(
            Q(type = query) | Q(currentState = query) 
        )
    if estado:
        queryset = queryset.filter(currentState = estado)
        
    if tipo:
        queryset = queryset.filter(type = tipo)
    
    if ordenar_por:
        queryset = queryset.order_by(ordenar_por)

    if fecha_creacion_inicio and fecha_creacion_fin:
        queryset = queryset.filter(
            creationDate__range=[fecha_creacion_inicio, fecha_creacion_fin]
        )
    if fecha_cierre_inicio and fecha_cierre_fin:
        queryset = queryset.filter(
            closeDate__range=[fecha_cierre_inicio, fecha_cierre_fin]
        )
        
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    followingData = Following.objects.all()
    try:
        followingData = paginator.page(page_number)
    except PageNotAnInteger:
        followingData = paginator.page(1)
    except EmptyPage:
        followingData = paginator.page(paginator.num_pages)
    
    queryset = Following.objects.none()
    
    # Obtener tipos únicos de los objetos de Following


    #followingData = Following.objects.all()
    #attachedDocuments = AttachedDocument.objects.all()
    tipos = Following.objects.values_list('type', flat=True).distinct()
    estados = State.objects.all()
    fechas_creacion = Following.objects.values_list('creationDate', flat=True).distinct()
    fechas_cierre = Following.objects.values_list('closeDate', flat=True).distinct()
    
    
    # Pasar objetos al contexto
    context = {
        'followingData': followingData,
        'estados': estados, 
        'tipos': tipos,  # Obtener los tipos únicos
        'fechas_creacion': fechas_creacion,
        'fechas_cierre': fechas_cierre,
    }
    
    return render(request, 'summaryOneStopShop.html', context)


def oneStopShopConfirmationView(request):
    return render(request, 'oneStopShopConfirmation.html')


def fullOneStopShopView(request):
    followingData = Following.objects.all()
    attachedDocuments = AttachedDocument.objects.all()

    return render(request, 'fullOneStopShop.html', {'followingData': followingData, 'files': attachedDocuments})

def oneStopShopConfirmationView(request):
    return render(request, 'oneStopShopConfirmation.html')

def oneStopShopFormView(request):
    if request.method == 'POST':
        oneStopShopForm = OneStopShopForm(request.POST)
        attachedDocumentForm = AttachedDocumentForm(request.POST, request.FILES)
        if oneStopShopForm.is_valid() and attachedDocumentForm.is_valid():
            following = oneStopShopForm.save()  
            attachedDocument = attachedDocumentForm.save(commit=False)
            attachedDocument.associatedFollowing = following 
            attachedDocument.save()  
            return redirect('confirmation')  
    else:
        oneStopShopForm = OneStopShopForm()
        attachedDocumentForm = AttachedDocumentForm()
    return render(request, 'oneStopShopForm.html', {'oneStopShopForm': oneStopShopForm, 'attachedDocumentForm': attachedDocumentForm})

