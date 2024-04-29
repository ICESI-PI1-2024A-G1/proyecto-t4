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
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
from openpyxl.drawing.image import Image
from openpyxl.utils import get_column_letter
from django.template.loader import get_template


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
        "Pago al exterior\n Universidad Icesi Nit. 890.316.745-5.",
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
        "Solicitud de cuenta de cobro\n Universidad Icesi Nit. 890.316.745-5.",
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
        "Solicitud de requisición\n Universidad Icesi Nit. 890.316.745-5.",
        email,
        "Requisición",
        createRequisitionForm
    )



def createLegalizationForm(request):
    TravelExpenseFormSet = inlineformset_factory(
        Legalization, LegalizationExpense,
        form=TravelExpenseForm, extra=1, can_delete=True
    )

    if request.method == 'POST':
        solicitation_form = TravelExpensesSolicitationForm(request.POST, request.FILES)
        expense_formset = TravelExpenseFormSet(request.POST, request.FILES, instance=None)

        if solicitation_form.is_valid() and expense_formset.is_valid():
            solicitation = solicitation_form.save()

            expenses = expense_formset.save(commit=False)
            for expense in expenses:
                expense.solicitation = solicitation
                expense.save()

            # Enviar el archivo Excel al correo
            sendLegalizationFormAsExcel(request, solicitation)

            return redirect('viewLegalizationForm')
    else:
        solicitation_form = TravelExpensesSolicitationForm()
        expense_formset = TravelExpenseFormSet()

    return render(request, 'legalizationForm.html', {
        'solicitation_form': solicitation_form,
        'expense_formset': expense_formset
    })
    

def createAdvancePaymentForm(request):
    
    TravelAdvanceExpenseFormSet = inlineformset_factory(
    AdvancePayment, AdvanceExpense,
    form=TravelAdvanceExpenseForm, extra=1, can_delete=True,
)

    if request.method == 'POST':
        solicitation_form = TravelAdvanceSolicitationForm(request.POST, request.FILES)
        expense_formset = TravelAdvanceExpenseFormSet(request.POST, request.FILES, instance=None)

        if solicitation_form.is_valid() and expense_formset.is_valid():
            solicitation = solicitation_form.save()

            expenses = expense_formset.save(commit=False)
            for expense in expenses:
                expense.solicitation = solicitation
                expense.save()

            # Enviar el archivo Excel al correo
            sendAdvancePaymentFormAsExcel(request, solicitation)

            return redirect('viewAdvancePaymentForm')
    else:
        solicitation_form =TravelAdvanceSolicitationForm()
        expense_formset = TravelAdvanceExpenseFormSet()

    return render(request, 'advancePaymentForm.html', {
        'solicitation_form': solicitation_form,
        'expense_formset': expense_formset
    })
    





def generateExcelAdvancePayment(solicitation):
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
    
    
    
    # Ancho de la columna
    column_letter = 'A'
    column_width = 11
    worksheet.column_dimensions[column_letter].width = column_width
    
    column_letter = 'B'
    column_width = 20
    worksheet.column_dimensions[column_letter].width = column_width
    
    column_letter = 'C'
    column_width = 20
    worksheet.column_dimensions[column_letter].width = column_width
    
    column_letter = 'D'
    column_width = 2
    worksheet.column_dimensions[column_letter].width = column_width
    
    column_letter = 'E'
    column_width = 23
    worksheet.column_dimensions[column_letter].width = column_width
    
    column_letter = 'F'
    column_width = 2
    worksheet.column_dimensions[column_letter].width = column_width
    
    column_letter = 'G'
    column_width = 33
    worksheet.column_dimensions[column_letter].width = column_width
    
    column_letter = 'H'
    column_width = 11
    worksheet.column_dimensions[column_letter].width = column_width
    
    #borde derecho de la solicitud       
    right_border = Border(
        right=Side(style='thin')   
    )
    start_row = 1
    end_row = 42
    
    for row in range(start_row, end_row + 1):
        for col in range(8, 8 + 1):
            cell = worksheet.cell(row=row, column=col)
            cell.border = right_border


    # Agregar una imagen al archivo Excel
    #image_path = 'SistemaContableApp\static\images\LogoIcesi.jpg'  # Reemplaza con la ruta de tu imagen
    #img = Image(image_path)
    #img_width, img_height = img.width, img.height


    # Escribir encabezados
    
    # Agregar Logo de icesi en la primera casilla
    #image_path = 'SistemaContableApp\static\images\LogoIcesi.jpg'  # Reemplaza con la ruta de tu imagen
    #img = Image(image_path)
    worksheet.merge_cells('A1:B4')
    merged_cell = worksheet['A1']
    #merged_cell.add_image(img,'A1' )
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    merged_cell.border = thin_border
    merged_cell.font = bold_font
    
    worksheet.merge_cells('C1:F2')
    merged_cell = worksheet['C1']
    merged_cell.value = 'CONTABILIDAD'
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    merged_cell.border = thin_border
    merged_cell.font = bold_font
    
    worksheet.merge_cells('C3:F4')
    merged_cell = worksheet['C3']
    merged_cell.value = 'FORMATO SOLICITUD DE ANTICIPO PARA GASTOS DE VIAJE'
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    merged_cell.border = thin_border
    merged_cell.font = bold_font
    
    worksheet.merge_cells('G1:H2')
    merged_cell = worksheet['G1']
    merged_cell.value = 'Código:\nCTA-FR-008'
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    merged_cell.border = thin_border
    merged_cell.font = bold_font
    
    worksheet.merge_cells('G3:H4')
    merged_cell = worksheet['G3']
    merged_cell.value = 'Versión:\n1.0'
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    merged_cell.border = thin_border
    merged_cell.font = bold_font
    

# -------------------------------------------parte de arriba del formato---------------------------------
    
    worksheet['B6'] = 'No. de Radicado'
    worksheet['B6'].font = bold_font
    worksheet['C6'].fill = PatternFill(start_color='DDEBF7', end_color='DDEBF7', fill_type='solid')
    worksheet['C6'] = solicitation.radicate
    worksheet['C6'].alignment = Alignment(horizontal='center', vertical='center')

    worksheet['E6'] = 'Código de Orden de pago'
    worksheet['E6'].font = bold_font
    worksheet.merge_cells('F6:G6')
    merged_cell = worksheet['F6']
    merged_cell.fill = PatternFill(start_color='DDEBF7', end_color='DDEBF7', fill_type='solid')
    worksheet['F6'] = solicitation.payment_order_code
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    
    worksheet['B8'] = 'Fecha de solicitud'
    worksheet['B8'].font = bold_font
    worksheet['C8'] = solicitation.request_date
    worksheet['C8'].alignment = Alignment(horizontal='center', vertical='center')

    worksheet['B9'] = 'Nombre del viajero'
    worksheet['B9'].font = bold_font
    worksheet.merge_cells('C9:G9')
    merged_cell = worksheet['C9']
    worksheet['C9'] = solicitation.traveler_name
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    
    worksheet['B10'] = 'No. de identificación'
    worksheet['B10'].font = bold_font
    worksheet.merge_cells('C10:D10')
    merged_cell = worksheet['C14']
    worksheet['C10'] = solicitation.traveler_id
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    
    worksheet['E10'] = 'Centro de Costos'
    worksheet['E10'].font = bold_font
    worksheet.merge_cells('F10:G10')
    merged_cell = worksheet['F10']
    worksheet['F10'] = solicitation.cost_center
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')

    worksheet['B11'] = 'Dependencia'
    worksheet['B11'].font = bold_font
    worksheet.merge_cells('C11:G11')
    merged_cell = worksheet['C11']
    worksheet['C11'] = solicitation.dependency
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')

    worksheet['B13'] = 'Ciudad de destino'
    worksheet['B13'].font = bold_font
    worksheet.merge_cells('C13:D13')
    merged_cell = worksheet['C13']
    worksheet['C13'] = solicitation.destiny_city
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')

    worksheet['B14'] = 'Fecha de Salida'
    worksheet['B14'].font = bold_font
    worksheet.merge_cells('C14:D14')
    merged_cell = worksheet['C14']
    worksheet['C14'] = solicitation.travel_date
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')

    worksheet['E14'] = 'Fecha de Regreso'
    worksheet['E14'].font = bold_font
    worksheet.merge_cells('F14:G14')
    merged_cell = worksheet['F14']
    worksheet['F14'] = solicitation.return_date
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')

    worksheet['B15'] = 'Motivo del Viaje'
    worksheet['B15'].font = bold_font
    worksheet.merge_cells('C15:G15')
    merged_cell = worksheet['C15']
    worksheet['C15'] = solicitation.motive
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    
    worksheet['B17'] = 'Tipo de moneda:'
    worksheet['B17'].font = bold_font
    worksheet.merge_cells('C17:G17')
    merged_cell = worksheet['C17']
    worksheet['C17'] = solicitation.currency_type_of_advance_value
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    
    worksheet.merge_cells('B18:D18')
    merged_cell = worksheet['B18']
    worksheet['B18'].value = 'Indique el último día que estará en Icesi antes de su viaje'
    worksheet.merge_cells('E18:G18')
    merged_cell = worksheet['E18']
    worksheet['E18'] = solicitation.last_day_in_icesi
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    
#------------------------ parte del formato media (tabla de gastos)--------------------------------------------------
    worksheet.merge_cells('C20:E20')
    merged_cell = worksheet['C20']
    worksheet['C20'] = 'PRESUPUESTO DE GASTOS'
    worksheet['C20'].font = bold_font
    worksheet['C20'].alignment = Alignment(horizontal='center', vertical='center')
    
    
    #Gris el valor de los gastos
    start_row = 21
    end_row = 29
    start_column = 5  # Columna A
    end_column = 5  # Columna H
    
    for row in range(start_row, end_row + 1):
        for col in range(start_column, end_column + 1):
            cell = worksheet.cell(row=row, column=col)
            cell.fill = PatternFill(start_color='D0CECE', end_color='D0CECE', fill_type='solid')
            cell.border = thin_border
    row = 21
    for expense in solicitation.expenses.all():
        worksheet.cell(row=row, column=3, value=expense.category)
        worksheet.cell(row=row, column=5, value=expense.money_value)

        row += 1
        
    worksheet['C29'].alignment = Alignment(horizontal='center', vertical='center')
    worksheet['C29'] = 'TOTAL DEL ANTICIPO'
    worksheet['C29'].font = bold_font
    worksheet['E29'].value ='=SUM(E21:E28)'
    worksheet['E29'].border = thin_border


    
    
#----------------------------------Parte de abajo del formato-------------------------------------------------------------------------
    worksheet.merge_cells('B30:G31')
    merged_cell = worksheet['B30']
    merged_cell.value = 'Autorización de descuento : Si pasados 15 días después de finalizar el viaje no he legalizado este anticipo;\n autorizo que su valor me sea descontado por nómina en lel mes más próximo.'
    
    
    top_border = Border(
        top=Side(style='thin')
    )
    
    worksheet['B34'] = 'Firma del viajero'
    worksheet['B34'].border = top_border
    worksheet['B34'].alignment = Alignment(horizontal='center', vertical='center')
    worksheet['B33'].alignment = Alignment(horizontal='center', vertical='center')
    worksheet['B33'] = solicitation.traveler_name
    
    worksheet['E34'] = 'Firma Ordenador de Gasto'
    worksheet['E34'].border = top_border
    worksheet['E34'].alignment = Alignment(horizontal='center', vertical='center')
    worksheet['E33'].alignment = Alignment(horizontal='center', vertical='center')
    worksheet['E33'] = solicitation.orderer_name

    worksheet['B37'] = 'Nombre de quien elabora'
    worksheet['B37'].border = top_border
    worksheet['B37'].alignment = Alignment(horizontal='center', vertical='center')
    worksheet['B36'].alignment = Alignment(horizontal='center', vertical='center')
    worksheet['B36'] = solicitation.orderer_name
    
    worksheet['E37'] = 'Nombre Ordenador de Gasto'
    worksheet['E37'].border = top_border
    worksheet['E37'].alignment = Alignment(horizontal='center', vertical='center')
    worksheet['E36'].alignment = Alignment(horizontal='center', vertical='center')
    worksheet['E36'] = solicitation.orderer_name
    
    
    worksheet.merge_cells('B39:G39')
    merged_cell = worksheet['B39']
    merged_cell.value = 'Campo de uso exclusivo de la Oficina de Contabilidad'
    merged_cell.font = bold_font  
    merged_cell.fill = PatternFill(start_color='D0CECE', end_color='D0CECE', fill_type='solid')
    
    worksheet.merge_cells('B40:G40')
    merged_cell = worksheet['B40']
    merged_cell.value = 'Motivo de devolución:'
    merged_cell.fill = PatternFill(start_color='D0CECE', end_color='D0CECE', fill_type='solid')
    
    
    
    worksheet.merge_cells('A42:H42')
    merged_cell = worksheet['A42']
    merged_cell.value = 'Espacio para ser diligenciado por la oficina de contabilidad:'
    merged_cell.font = bold_font  
    merged_cell.fill = PatternFill(start_color='DDEBF7', end_color='DDEBF7', fill_type='solid')
    
    
    # Guardar el archivo Excel
    filename = f'media/advancePayment_{solicitation.id}.xlsx'
    workbook.save(filename)
    return filename


 



def generateExcelLegalization(solicitation):
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
    end_column = 9  # Columna H
    
    for row in range(start_row, end_row + 1):
        for col in range(start_column, end_column + 1):
            cell = worksheet.cell(row=row, column=col)
            cell.border = thin_border
            
     
    #borde derecho de la solicitud       
    right_border = Border(
        right=Side(style='thin')   
    )
    start_row = 1
    end_row = 48
    
    for row in range(start_row, end_row + 1):
        for col in range(9, 9 + 1):
            cell = worksheet.cell(row=row, column=col)
            cell.border = right_border
            
            
    
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
    #image_path = 'SistemaContableApp\static\images\LogoIcesi.jpg'  # Reemplaza con la ruta de tu imagen
    #img = Image(image_path)
    #img_width, img_height = img.width, img.height


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
    merged_cell.border = thin_border
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')

    worksheet.merge_cells('B18:B19')
    merged_cell = worksheet['B18']
    merged_cell.value = '# de\nsoporte'
    merged_cell.fill = PatternFill(start_color='D0CECE', end_color='D0CECE', fill_type='solid')
    merged_cell.border = thin_border
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    merged_cell.font = bold_font
    
    worksheet.merge_cells('C18:C19')
    merged_cell = worksheet['C18']
    merged_cell.value = 'Nombre del tercero\nde la factura'
    merged_cell.fill = PatternFill(start_color='D0CECE', end_color='D0CECE', fill_type='solid')
    merged_cell.border = thin_border
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    merged_cell.font = bold_font 
    
    worksheet.merge_cells('D18:D19')
    merged_cell = worksheet['D18']
    merged_cell.value = 'NIT del\ntercero\nde la factura'
    merged_cell.fill = PatternFill(start_color='D0CECE', end_color='D0CECE', fill_type='solid')
    merged_cell.border = thin_border
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    merged_cell.font = bold_font    
    
    worksheet.merge_cells('E18:E19')
    merged_cell = worksheet['E18']
    merged_cell.value = 'Concepto de la compra'
    merged_cell.fill = PatternFill(start_color='D0CECE', end_color='D0CECE', fill_type='solid')
    merged_cell.border = thin_border
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    merged_cell.font = bold_font 
    
    worksheet.merge_cells('F18:H18')
    merged_cell = worksheet['F18']
    merged_cell.value = 'Si su anticipo fue en:'
    merged_cell.fill = PatternFill(start_color='D0CECE', end_color='D0CECE', fill_type='solid')
    merged_cell.border = thin_border
    merged_cell.alignment = Alignment(horizontal='center', vertical='center')
    merged_cell.font = bold_font 
    

    worksheet['F19'] = 'Pesos\ncolombianos'
    worksheet['F19'].border = thin_border
    
    worksheet['G19'] = 'Dólares'
    worksheet['G19'].border = thin_border
    
    worksheet['H19'] = 'Euros'
    worksheet['H19'].border = thin_border

    
    
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
    if solicitation.currency_type_of_advance_value == 'PESOS COLOMBIANOS':

        worksheet['F32'] = solicitation.advance_payment_value  # Valor de anticipo en pesos colombianos
        worksheet['G32'] = 0  # Valor de anticipo en dólares
        worksheet['H32'] = 0  # Valor de anticipo en euros
        
    elif solicitation.currency_type_of_advance_value == 'DOLARES':
        
        worksheet['F32'] = 0  # Valor de anticipo en pesos colombianos
        worksheet['G32'] = solicitation.advance_payment_value  # Valor de anticipo en dólares
        worksheet['H32'] = 0  # Valor de anticipo en euros
        
    elif solicitation.currency_type_of_advance_value == 'EUROS':
        
        worksheet['F32'] = 0  # Valor de anticipo en pesos colombianos
        worksheet['G32'] = 0  # Valor de anticipo en dólares
        worksheet['H32'] = solicitation.advance_payment_value  # Valor de anticipo en euros
        
    
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
    
    
    if solicitation.descount_in_one_quote == 1:
        worksheet['C38'].value = 'SÍ autorizo'
        worksheet['C38'].fill = PatternFill(start_color='C6E0B4', end_color='C6E0B4', fill_type='solid')
    elif solicitation.descount_in_one_quote == 0:
        worksheet['C38'].value = 'NO autorizo'
        worksheet['C38'].fill = PatternFill(start_color='FFABAB', end_color='FFABAB', fill_type='solid')
    
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
    filename = f'media/legalizacion_{solicitation.id}.xlsx'
    workbook.save(filename)
    return filename


def sendLegalizationFormAsExcel(request, solicitation):
    """
    Function to send the travel expenses solicitation as an Excel file.
    
    Args:
        request (HttpRequest): HTTP request object.
        solicitation (TravelExpensesSolicitation): Travel expenses solicitation instance.
    
    Returns:
        None
    """
    # Generar archivo Excel
    excel_filename = generateExcelLegalization(solicitation)

    # Enviar correo electrónico con el archivo Excel adjunto
    email = EmailMessage(
        'Solicitud de gastos de viaje',
        'Adjunto se encuentra la solicitud de gastos de viaje en formato Excel.\n Universidad Icesi Nit. 890.316.745-5.',
        settings.DEFAULT_FROM_EMAIL,
        to=["pinedapablo6718@gmail.com"]
    )
    email.attach_file(excel_filename)
    
    # Adjuntar archivos de cada gasto
    for expense in solicitation.expenses.all():
        if expense.support:
            email.attach_file(expense.support.path)

    try:
        email.send()
        messages.success(request, 'La solicitud de gastos de viaje se envió correctamente.')
    except Exception as e:
        messages.error(request, 'Error al enviar la solicitud de gastos de viaje.')
        
        
        
def sendAdvancePaymentFormAsExcel(request, solicitation) :
    """
    Function to send the travel expenses solicitation as an Excel file.
    
    Args:
        request (HttpRequest): HTTP request object.
        solicitation (TravelExpensesSolicitation): Travel expenses solicitation instance.
    
    Returns:
        None
    """
    # Generar archivo Excel
    excel_filename = generateExcelAdvancePayment(solicitation)

    # Enviar correo electrónico con el archivo Excel adjunto
    email = EmailMessage(
        'Solicitud de gastos de viaje',
        'Adjunto se encuentra la solicitud de anticipo para gastos de viaje en formato Excel.\n Universidad Icesi Nit. 890.316.745-5.',
        settings.DEFAULT_FROM_EMAIL,
        to=["pinedapablo6718@gmail.com"]
    )
    email.attach_file(excel_filename)
    

    try:
        email.send()
        messages.success(request, 'La solicitud de anticipo para gastos de viaje se envió correctamente.')
    except Exception as e:
        messages.error(request, 'Error al enviar la solicitud de anticipo para gastos de viaje.')
        
        