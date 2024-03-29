from django.shortcuts import render
from .models import  Charge_account,Following

from django.db.models import Q  
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect   
from .forms import CreateNewTask
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CreateNewTask, ChargeAccountForm
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


def ventanilla_unica(request):
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
            Q(state__icontains=query) | Q(type__icontains=query)
        )
    if estado:
        queryset = queryset.filter(state=estado)
    if tipo:
        queryset = queryset.filter(type__contains= tipo)
    
    if ordenar_por:
        queryset = queryset.order_by(ordenar_por)

    if fecha_creacion_inicio and fecha_creacion_fin:
        queryset = queryset.filter(
            creation_date__range=[fecha_creacion_inicio, fecha_creacion_fin]
        )
    if fecha_cierre_inicio and fecha_cierre_fin:
        queryset = queryset.filter(
            close_date__range=[fecha_cierre_inicio, fecha_cierre_fin]
        )
        

    
    # Configurar la paginación
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    try:
        ventanilla = paginator.page(page_number)
    except PageNotAnInteger:
        ventanilla = paginator.page(1)
    except EmptyPage:
        ventanilla = paginator.page(paginator.num_pages)
    
    # Obtener tipos únicos de los objetos de Following
    tipos = Following.objects.values_list('type', flat=True).distinct()
    estados = Following.ESTADOS
    fechas_creacion = Following.objects.values_list('creation_date', flat=True).distinct()
    fechas_cierre = Following.objects.values_list('close_date', flat=True).distinct()
    
    
    # Pasar objetos al contexto
    context = {
        'ventanilla': ventanilla,
        'estados': estados, 
        'tipos': tipos,  # Obtener los tipos únicos
        'fechas_creacion': fechas_creacion,
        'fechas_cierre': fechas_cierre,
    }
    
    return render(request, 'ventanilla_unica_resumida.html', context)


#con esta verga no funciona, con la de arriba sí


#def args_principal(seleccionado):
    #return {
        #"Programas posgrado": {"url": "/academico/programas", "seleccionado": seleccionado=="programas"},
        #"Materias posgrado": {"url": "/academico/materias", "seleccionado": seleccionado=="materias"},
        #"Docentes posgrado": {"url": "/docentes", "seleccionado": seleccionado=="docentes"}
        #}