from django.conf import settings 
from SistemaContableApp.models import  *
from SistemaContableApp.forms import *
from django.template.loader import get_template  
from django.shortcuts import render, redirect
from django.core.mail import  EmailMessage 
from django.contrib import messages
import weasyprint
from weasyprint import HTML, CSS
from django.core.files.storage import default_storage

def sendFormAsPdf(request, template_name, css_file, subject, recipient_email, form_data, pdf_filename, form_instance):
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
        form_instance (Model): The instance of the form model.

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

    # Attach the uploaded files
    for field in form_instance._meta.get_fields():
        if isinstance(field, models.FileField):
            file_field = getattr(form_instance, field.name)
            if file_field:
                file_path = default_storage.path(file_field.name)
                email.attach_file(file_path)

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
            sendFormAsPdf(request, pdf_template_name, css_file, subject, recipient_email, form_data, pdf_filename, form_instance)
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

def createLegalizationForm(request):
    TravelExpenseFormSet = inlineformset_factory(
        Legalization, LegalizationExpense,
        form=TravelExpenseForm, extra=1
    )

    if request.method == 'POST':
        solicitation_form = TravelExpensesSolicitationForm(request.POST, request.FILES)
        if solicitation_form.is_valid():
            solicitation = solicitation_form.save(commit=False)
            expense_formset = TravelExpenseFormSet(request.POST, request.FILES, instance=solicitation)
            if expense_formset.is_valid():
                solicitation.save()
                expense_formset.save()
                # Enviar el archivo Excel al correo
                send_travel_expenses_solicitation_as_excel(request, solicitation)
                
                return redirect('viewLegalizationForm')
    else:
        solicitation_form = TravelExpensesSolicitationForm()
        expense_formset = TravelExpenseFormSet()

    return render(request, 'legalizationForm.html', {
        'solicitation_form': solicitation_form,
        'expense_formset': expense_formset
    })

    


'''
def send_travel_expenses_solicitation_as_pdf(request, solicitation):
    """
    Function to send the travel expenses solicitation as a PDF email.
    
    Args:
        request (HttpRequest): HTTP request object.
        solicitation (TravelExpensesSolicitation): Travel expenses solicitation instance.
    
    Returns:
        None
    """
    # Renderizar el HTML del correo electrónico
    html_template = 'send_travel_expenses_solicitation_email.html'
    html_content = get_template(html_template).render({'object': solicitation})

    # Convertir a PDF
    #css_file = 'SistemaContableApp/static/styles/send_travel_expenses_solicitation_email.css'
    #css = CSS(filename=css_file)
    pdf = HTML(string=html_content).write_pdf()

    # Enviar correo electrónico con PDF adjunto
    email = EmailMessage(
        'Solicitud de gastos de viaje',
        'Adjunto se encuentra la solicitud de gastos de viaje.',
        settings.DEFAULT_FROM_EMAIL,
        to =["pinedapablo6718@gmail.com"]
    )
    email.attach('solicitud_gastos_viaje.pdf', pdf, 'application/pdf')

    try:
        email.send()
        messages.success(request, 'La solicitud de gastos de viaje se envió correctamente.')
    except Exception as e:
        messages.error(request, 'Error al enviar la solicitud de gastos de viaje.')

def travel_expenses_solicitation_list(request):
    solicitations = Legalization.objects.all()
    return render(request, 'travel_expenses_solicitation_list.html', {'solicitations': solicitations})

def travel_expenses_solicitation_detail(request, pk):
    solicitation = Legalization.objects.get(pk=pk)
    return render(request, 'travel_expenses_solicitation_detail.html', {'solicitation': solicitation})
'''


from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
from openpyxl.drawing.image import Image
from openpyxl.utils import get_column_letter
from django.conf import settings
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.contrib import messages

def generate_excel_report(solicitation):
    workbook = Workbook()
    worksheet = workbook.active
    
    
    
    #estilo de los bordes de la casilla
    bold_font = Font(bold=True)
    
    thin_border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
    
    #Aplicarle bordes de las casillas de la tabla de gastos
    start_row = 20
    end_row = 34
    start_column = 1  # Columna A
    end_column = 8  # Columna H
    
    for row in range(start_row, end_row + 1):
        for col in range(start_column, end_column + 1):
            cell = worksheet.cell(row=row, column=col)
            cell.border = thin_border
            
            
    
    # Ancho de la columna
    column_letter = 'A'
    column_width = 32
    worksheet.column_dimensions[column_letter].width = column_width
    
    column_letter = 'B'
    column_width = 9
    worksheet.column_dimensions[column_letter].width = column_width
    
    column_letter = 'C'
    column_width = 18
    worksheet.column_dimensions[column_letter].width = column_width
    
    column_letter = 'D'
    column_width = 14
    worksheet.column_dimensions[column_letter].width = column_width
    
    column_letter = 'E'
    column_width = 38
    worksheet.column_dimensions[column_letter].width = column_width
    
    column_letter = 'F'
    column_width = 11
    worksheet.column_dimensions[column_letter].width = column_width
    
    column_letter = 'G'
    column_width = 11
    worksheet.column_dimensions[column_letter].width = column_width
    
    column_letter = 'H'
    column_width = 11
    worksheet.column_dimensions[column_letter].width = column_width
    
    column_letter = 'I'
    column_width = 11
    worksheet.column_dimensions[column_letter].width = column_width



    # Agregar una imagen al archivo Excel
    image_path = 'SistemaContableApp\static\images\LogoIcesi.jpg'  # Reemplaza con la ruta de tu imagen
    img = Image(image_path)
    img_width, img_height = img.width, img.height


    # Escribir encabezados
    
    # Agregar Logo de icesi en la primera casilla
    #image_path = 'SistemaContableApp\static\images\LogoIcesi.jpg'  # Reemplaza con la ruta de tu imagen
    #img = Image(image_path)
    worksheet.merge_cells('A1:A4')
    merged_cell = worksheet['A1']
    #merged_cell.add_image(img,'A1' )
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    merged_cell.border = thin_border
    merged_cell.font = bold_font
    
    worksheet.merge_cells('B1:G2')
    merged_cell = worksheet['B1']
    merged_cell.value = 'CONTABILIDAD'
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    merged_cell.border = thin_border
    merged_cell.font = bold_font
    
    worksheet.merge_cells('B3:G4')
    merged_cell = worksheet['B3']
    merged_cell.value = 'FORMATO DE LEGALIZACIÓN DE GASTOS DE VIAJE'
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    merged_cell.border = thin_border
    merged_cell.font = bold_font
    
    worksheet.merge_cells('H1:I2')
    merged_cell = worksheet['H1']
    merged_cell.value = 'Código:\nCTA-FR-008'
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    merged_cell.border = thin_border
    merged_cell.font = bold_font
    
    worksheet.merge_cells('H3:I4')
    merged_cell = worksheet['H3']
    merged_cell.value = 'Versión:\n1.0'
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    merged_cell.border = thin_border
    merged_cell.font = bold_font
    
    

    
    
    # -------------------------------------------parte de arriba del formato---------------------------------
    worksheet['A6'] = 'Fecha de legalización'
    worksheet['A6'].font = bold_font
    worksheet['B6'] = solicitation.legalization_date

    
    worksheet['A7'] = 'Nombre del viajero'
    worksheet['A7'].font = bold_font
    worksheet['B7'] = solicitation.traveler_name

    worksheet['A8'] = 'No. de Identificación'
    worksheet['A8'].font = bold_font
    worksheet['B8'] = solicitation.identification

    worksheet['E8'] = 'Centro de Costos'
    worksheet['E8'].font = bold_font
    worksheet['F8'] = solicitation.cost_center

    worksheet['A9'] = 'Dependencia'
    worksheet['A9'].font = bold_font
    worksheet['B9'] = solicitation.dependency

    worksheet['A11'] = 'Ciudad de destino'
    worksheet['A11'].font = bold_font
    worksheet['B11'] = solicitation.destiny_city

    worksheet['A12'] = 'Fecha de Salida'
    worksheet['A12'].font = bold_font
    worksheet['B12'] = solicitation.travel_date

    worksheet['E12'] = 'Fecha de Regreso'
    worksheet['E12'].font = bold_font
    worksheet['F12'] = solicitation.return_date

    worksheet['A13'] = 'Motivo del Viaje'
    worksheet['A13'].font = bold_font
    worksheet['B13'] = solicitation.motive
    

    #------------------------ parte del formato media (tabla de gastos)--------------------------------------------------
    worksheet['A16'] = 'Relación de gastos'
    worksheet['A16'].font = bold_font
    worksheet['A16'].fill = PatternFill(start_color='D0CECE', end_color='D0CECE', fill_type='solid')
    worksheet['A16'].alignment = Alignment(horizontal='center', vertical='center')
    
    
    worksheet.merge_cells('A18:A19')
    merged_cell = worksheet['A18']
    merged_cell.value = 'Rubro'
    merged_cell.font = bold_font
    merged_cell.fill = PatternFill(start_color='D0CECE', end_color='D0CECE', fill_type='solid')
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')

    worksheet.merge_cells('B18:B19')
    merged_cell = worksheet['B18']
    merged_cell.value = '# de\nsoporte'
    merged_cell.fill = PatternFill(start_color='D0CECE', end_color='D0CECE', fill_type='solid')
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    merged_cell.font = bold_font
    
    worksheet.merge_cells('C18:C19')
    merged_cell = worksheet['C18']
    merged_cell.value = 'Nombre del tercero\nde la factura'
    merged_cell.fill = PatternFill(start_color='D0CECE', end_color='D0CECE', fill_type='solid')
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    merged_cell.font = bold_font 
    
    worksheet.merge_cells('D18:D19')
    merged_cell = worksheet['D18']
    merged_cell.value = 'NIT del\ntercero\nde la factura'
    merged_cell.fill = PatternFill(start_color='D0CECE', end_color='D0CECE', fill_type='solid')
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    merged_cell.font = bold_font    
    
    worksheet.merge_cells('E18:E19')
    merged_cell = worksheet['E18']
    merged_cell.value = 'Concepto de la compra'
    merged_cell.fill = PatternFill(start_color='D0CECE', end_color='D0CECE', fill_type='solid')
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    merged_cell.font = bold_font 
    
    worksheet.merge_cells('F18:H18')
    merged_cell = worksheet['F18']
    merged_cell.value = 'Si su anticipo fue en:'
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    merged_cell.font = bold_font 
    

    worksheet['F19'] = 'Pesos\ncolombianos'
    worksheet['G19'] = 'Dólares'
    worksheet['H19'] = 'Euros'

    
    
    row = 20
    for expense in solicitation.expenses.all():
        worksheet.cell(row=row, column=1, value=expense.category)
        worksheet.cell(row=row, column=2, value=expense.support_no)
        worksheet.cell(row=row, column=3, value=expense.third_person_name)
        worksheet.cell(row=row, column=4, value=expense.third_person_nit)
        worksheet.cell(row=row, column=5, value=expense.concept)

        # Diferencia el valor de money_value según el tipo de moneda
        if expense.money_type == 'PESOS COLOMBIANOS':
            worksheet.cell(row=row, column=6, value=expense.money_value)
        elif expense.money_type == 'DOLARES':
            worksheet.cell(row=row, column=7, value=expense.money_value)
        elif expense.money_type == 'EUROS':
            worksheet.cell(row=row, column=8, value=expense.money_value)

        row += 1
            

    # Total de gastos
    worksheet['A31'] = 'Total de gastos'
    worksheet['F31'].value = '=SUM(F20:F30)'  # Suma de pesos colombianos
    worksheet['G31'].value = '=SUM(G20:G30)'  # Suma de dólares
    worksheet['H31'].value = '=SUM(H20:H30)'  # Suma de euros
    
    
    #color gris para la parte de total de gastos
    start_row = 31
    end_row = 31
    start_column = 1  # Columna A
    end_column = 8  # Columna H
    
    for col in range(start_row, end_row + 1):
        for row in range(start_column, end_column + 1):
            cell = worksheet.cell(row=row, column=col)
            cell.fill = PatternFill(start_color='D0CECE', end_color='D0CECE', fill_type='solid')
       
          
    # Valor del anticipo
    worksheet['A32'] = 'Valor del anticipo'
    worksheet['F32'] = '0'  # Valor de anticipo en pesos colombianos
    worksheet['G32'] = '0'  # Valor de anticipo en dólares
    worksheet['H32'] = '0'  # Valor de anticipo en euros
    
    #color azul para la parte de valor de anticipo
    
    
    start_row = 32
    end_row = 32
    start_column = 1  # Columna A
    end_column = 8  # Columna H
    
    for col in range(start_row, end_row + 1):
        for row in range(start_column, end_column + 1):
            cell = worksheet.cell(row=row, column=col)
            cell.fill = PatternFill(start_color='DDEBF7', end_color='DDEBF7', fill_type='solid')
  

    # Saldo a favor del empleado
    worksheet['A33'] = 'Saldo a favor del empleado'
    worksheet['F33'].value = '=IF(F31>F32,F31-F32,0)'  # Saldo en pesos colombianos
    worksheet['G33'].value = '=IF(G31>G32,G31-G32,0)'  # Saldo en dólares
    worksheet['H33'].value = '=IF(H31>H32,H31-H32,0)'  # Saldo en euros

    # Saldo a favor de ICESI
    worksheet['A34'] = 'Saldo a favor de ICESI'
    worksheet['F34'].value = '=IF(F31<F32,F32-F31,0)'  # Saldo en pesos colombianos
    worksheet['G34'].value = '=IF(G31<G32,G32-G31,0)'  # Saldo en dólares
    worksheet['H34'].value = '=IF(H31<H32,H32-H31,0)'  # Saldo en euros

    

    #----------------------------------Parte de abajo del formato-------------------------------------------------------------------------
    worksheet.merge_cells('A36:E37')
    merged_cell = worksheet['A36']
    merged_cell.value = 'Autorizo que el saldo a favor de la Universidad Icesi, sea descontado en una sola\ncuota en el siguiente pago de nómina.'
    
    
    if solicitation.descount_in_one_quote == 'TRUE':
        worksheet['C38'] = 'SÍ autorizo'
        worksheet['C38'].fill = PatternFill(start_color='C6E0B4', end_color='DDEBF7', fill_type='solid')
    else:
        worksheet['C38'] = 'NO autorizo'
        worksheet['C38'].fill = PatternFill(start_color='FFABAB', end_color='DDEBF7', fill_type='solid')
    
    top_border = Border(
        top=Side(style='thin')
    )
    
    worksheet['A41'] = 'Nombre de quien elabora'
    worksheet['A41'].border = top_border
    worksheet['A41'].alignment = Alignment(horizontal='center', vertical='center')
    worksheet['A40'].alignment = Alignment(horizontal='center', vertical='center')
    worksheet['A40'] = solicitation.elaborator_name
    
    worksheet['E41'] = 'Nombre Ordenador de gasto'
    worksheet['E41'].border = top_border
    worksheet['E41'].alignment = Alignment(horizontal='center', vertical='center')
    worksheet['E40'].alignment = Alignment(horizontal='center', vertical='center')
    worksheet['E40'] = solicitation.orderer_name
    
    
    worksheet['A45'] = 'Banco'
    worksheet['A45'].font = bold_font  
    worksheet['B45'] = solicitation.bank
    
    worksheet['A46'] = '# de cuenta'
    worksheet['A46'].font = bold_font  
    worksheet['B46'] = solicitation.account_number
    
    worksheet['D45'] = 'Tipo de cuenta'
    worksheet['D45'].font = bold_font  
    worksheet['E45'] = solicitation.type_account
    
    
    worksheet.merge_cells('A48:I48')
    merged_cell = worksheet['A48']
    merged_cell.value = 'OBSERVACIONES:'
    merged_cell.font = bold_font  
    merged_cell.fill = PatternFill(start_color='DDEBF7', end_color='DDEBF7', fill_type='solid')
    
    
    



    # Guardar el archivo Excel
    filename = f'legalizacion_{solicitation.id}.xlsx'
    workbook.save(filename)
    return filename





def send_travel_expenses_solicitation_as_excel(request, solicitation):
    """
    Function to send the travel expenses solicitation as an Excel file.
    
    Args:
        request (HttpRequest): HTTP request object.
        solicitation (TravelExpensesSolicitation): Travel expenses solicitation instance.
    
    Returns:
        None
    """
    # Generar archivo Excel
    excel_filename = generate_excel_report(solicitation)

    # Enviar correo electrónico con el archivo Excel adjunto
    email = EmailMessage(
        'Solicitud de gastos de viaje',
        'Adjunto se encuentra la solicitud de gastos de viaje en formato Excel.',
        settings.DEFAULT_FROM_EMAIL,
        to=["pinedapablo6718@gmail.com"]
    )
    email.attach_file(excel_filename)

    try:
        email.send()
        messages.success(request, 'La solicitud de gastos de viaje se envió correctamente.')
    except Exception as e:
        messages.error(request, 'Error al enviar la solicitud de gastos de viaje.')