from django.contrib.auth import authenticate, login
from .models import  *
from django.db.models import Q  
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect   
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
from weasyprint import HTML, CSS
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView

def index(request):
    """
    View for the home page.

    Displays the home page of the accounting system.

    Args:
        request (HttpRequest): The received HTTP request.

    Returns:
        HttpResponse: The HTTP response rendering the home page.
  
    """
    
    title = "¡Bienvenidos al Sistema Contable"
    return render(request,'index.html', {
        'title' : title 
    })


def olvidar_contraseña(request):
    """
    View for the forgot password page.

    Displays the forgot password page.

    Args:
        request (HttpRequest): The received HTTP request.

    Returns:
        HttpResponse: The HTTP response rendering the forgot password page.
    """
    return render(request,'registration/password_reset_form.html' )


def user_login(request):
    """
    View for user login.

    Processes the login form and authenticates the user.

    Args:
        request (HttpRequest): The received HTTP request.

    Returns:
        HttpResponse: Redirects to the home page if login is successful, 
                      otherwise redirects to the login page.
    """
   
    if request.method == 'POST':
        email = request.POST.get('email')  
        password = request.POST.get('password')
        user = authenticate(request,
                            username=request.POST['email'],
                            password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(index)  
            else:
                messages.error(request, 'El usuario no está activo')
                return redirect('index') 
        else:
            messages.error(request, 'No tienes una cuenta, por favor registrate')
            return redirect('index') 
    else:
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})          
           
@login_required
def dashboard(request):
    return render(request,'index.html')
    

def registration(request):
        """
        View for user registration.

        Processes the user registration form and creates a new user account.

        Args:
            request (HttpRequest): The received HTTP request.

        Returns:
            HttpResponse: Redirects to the home page if registration is successful,
                        otherwise redirects to the registration page.
        """
        
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                messages.success(request, 'Tu cuenta ha sido creada exitosamente.')
                login(request, user)
                messages.success(request, 'Registro exitoso.')
                return redirect('index')
            else:
                messages.error(request, 'Error en el registro. Por favor, revise los datos introducidos.')
        else:
            form = CustomUserCreationForm()
        return render(request, 'registration/registrationUsers.html', {'form': form})

def password_reset_request(request):
    """
    View for requesting a password reset.

    Processes the password reset request form and sends an email with instructions
    to reset the password.

    Args:
        request (HttpRequest): The received HTTP request.

    Returns:
        HttpResponse: Redirects to the password reset done page if the request is
                      successful, otherwise renders the password reset form page.
    """
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            # Django's password reset form already includes functionality to send the email
            password_reset_form.save(
                request=request,
                use_https=False,
                email_template_name='registration/password_reset_email.html',
            )
            return redirect('password_reset_done')
    else:
        password_reset_form = PasswordResetForm()
    return render(request, 'registration/password_reset_form.html', {'form': password_reset_form})
 
 
   
def sendFormAsPdf(request, template_name, css_file, subject, recipient_email, form_data, pdf_filename):
    """
    Function to send a form as a PDF email.

    Args:
        request (HttpRequest): HTTP request object.
        template_name (str): Name of the HTML template to generate the message body.
        css_file (str): Path to the CSS file to apply styles to the PDF.
        subject (str): Subject of the email.
        recipient_email (str): Email address of the recipient.
        form_data (dict): Form data.
        pdf_filename (str): Name of the PDF file.

    Returns:
        None
    """
    
    message_body = get_template(template_name).render(form_data)
    css = CSS(filename=css_file)
    pdf = weasyprint.HTML(string=message_body).write_pdf(stylesheets=[css])

    email = EmailMessage(
        subject,
        "Aqui se encuentra una solicitud requerida",
        settings.DEFAULT_FROM_EMAIL,
        to=[recipient_email]
    )
    email.attach(f'{pdf_filename}.pdf', pdf, 'application/pdf')
    try:
        email.send()
        messages.success(request, 'la solicitud se envió correctamente a ventanilla unica')
    except Exception as e:
        messages.error(request, 'Error al enviar la solicitud a ventanilla unica')


def createForm(request, form_class, template_name, pdf_template_name, css_file, subject, recipient_email, pdf_filename, redirectTo):
    """
    Function to create a form and send it as a PDF email.

    Args:
        request (HttpRequest): HTTP request object.
        form_class (forms.ModelForm): Form class.
        template_name (str): Name of the HTML template to render the form.
        pdf_template_name (str): Name of the HTML template to generate the PDF body.
        css_file (str): Path to the CSS file to apply styles to the PDF.
        subject (str): Subject of the email.
        recipient_email (str): Email address of the recipient.
        pdf_filename (str): Name of the PDF file.
        redirectTo (str): URL to redirect to after sending the form.

    Returns:
        HttpResponse: HTTP response with the form or success/error message.
    """
    
    if request.method == "POST":
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.save()
            form_data = form.cleaned_data
            sendFormAsPdf(request, pdf_template_name, css_file, subject, recipient_email, form_data, pdf_filename)
            messages.success(request, 'El formulario se ha creado correctamente y se ha enviado en pdf.')
            return redirect(redirectTo)
        else:
            form = form_class()
            messages.error(request, 'Error al crear el formulario.')
            return render(request, template_name, {"form": form})
    else:
        form = form_class()
        return render(request, template_name, {"form": form})


email = "pinedapablo6718@gmail.com"
email2 = "daniela32156@hotmail.com"


def createExteriorPaymentForm(request):
    """
    View that displays the form to create an exterior payment request.

    Args:
        request (HttpRequest): HTTP request object.

    Returns:
        HttpResponse: HTTP response with the form or success/error message.
    """
    return createForm(
        request,
        ExteriorPaymentForm,
        "exteriorPaymentForm.html",
        "sendExteriorPaymentForm.html",
        "SistemaContableApp/static/styles/sendExteriorPaymentForm.css",
        "Solicitud de requisición de pago al exterior",
        email,
        "Pago al exterior",
        createExteriorPaymentForm
    )

def createChargeAccountForm(request):
    """
    View that displays the form to create a charge account request.

    Args:
        request (HttpRequest): HTTP request object.

    Returns:
        HttpResponse: HTTP response with the form or success/error message. 
    """ 
    return createForm(
        request,
        ChargeAccountForm,
        "chargeAccountForm.html",
        "sendChargeAccountForm.html",
        "SistemaContableApp/static/styles/sendChargeAccountForm.css",
        "Solicitud de cuenta de cobro",
        email,
        "Cuenta de cobro",
        createChargeAccountForm
    )
    
def createRequisitionForm(request):
    """
    View that displays the form to create a requisition request.

    Args:
        request (HttpRequest): HTTP request object.

    Returns:
        HttpResponse: HTTP response with the form or success/error message.
    """
    
    return createForm(
        request,
        RequisitionForm,
        "requisitionForm.html",
        "sendRequisitionForm.html",
        "SistemaContableApp/static/styles/sendRequisitionForm.css",
        "Solicitud de requisición",
        email,
        "Requisición",
        createRequisitionForm
    )

"""    
   
    
def createAdvanceForm(request):
    return createForm(
        request,
        AdvanceForm,
        "advanceForm.html",
        "sendAdvanceForm.html",
        "SistemaContableApp/static/styles/sendAdvanceForm.css",
        "Solicitud de anticipo",
        email,
        "Anticipo",
        createAdvanceForm
    )
    
def createLegalizationForm(request):
    return createForm(
        request,
        LegalizationForm,
        "legalizationForm.html",
        "sendLegalizationForm.html",
        "SistemaContableApp/static/styles/sendLegalizationForm.css",
        "Solicitud de legalización de gastos de viaje",
        email,
        "Legalización de gastos de viaje",
        createLegalizationForm
    )
"""


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


def oneStopShopFormView(request):
    if request.method == 'POST':
        oneStopShopForm = OneStopShopForm(request.POST)
        attachedDocumentForm = AttachedDocumentForm(request.POST, request.FILES)
        if oneStopShopForm.is_valid() and attachedDocumentForm.is_valid():
            following = oneStopShopForm.save()  
            attachedDocument = attachedDocumentForm.save(commit=False)
            attachedDocument.associatedFollowing = following 
            attachedDocument.save()
            return redirect('OneStopShopForm')  
        else:
            oneStopShopForm = OneStopShopForm()
            attachedDocumentForm = AttachedDocumentForm()
            return render(request, 'oneStopShopForm.html', {'oneStopShopForm': oneStopShopForm, 'attachedDocumentForm': attachedDocumentForm})
    else:
        oneStopShopForm = OneStopShopForm()
        attachedDocumentForm = AttachedDocumentForm()
        return render(request, 'oneStopShopForm.html', {'oneStopShopForm': oneStopShopForm, 'attachedDocumentForm': attachedDocumentForm})

