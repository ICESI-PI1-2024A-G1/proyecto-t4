from django.shortcuts import render
from .models import  Charge_account


from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect   
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import ChargeAccountForm, RequisitionForm
from django.conf import settings 
from django.template.loader import get_template  
from django.core.mail import get_connection, EmailMessage
from django.template.loader import get_template
from django.conf import settings
from django.core.mail import EmailMessage
import weasyprint
from weasyprint import HTML, CSS

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


email="pinedapablo6718@gmail.com"

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
        "sendChargeAccountForm.html",
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
def createExteriorPaymentForm(request):
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