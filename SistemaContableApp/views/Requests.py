from datetime import date, datetime
from django.conf import settings 
from SistemaContableApp.models import  *
from SistemaContableApp.forms import *
from django.template.loader import get_template  
from django.shortcuts import render, redirect
from django.core.mail import  EmailMessage 
from django.contrib import messages
import weasyprint
from weasyprint import  CSS





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
            request_date = datetime.now()
            
            if isLateRequest(request_date):
                messages.success(request, 'Su solicitud se ha programado para el siguiente mes, ya que se recibió después del día 20 del mes.')
            
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

def isLateRequest(request_date):
    today = date.today()
    if request_date.day > 20 and request_date.month == today.month:
        return True
    return False


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