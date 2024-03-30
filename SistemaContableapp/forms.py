from django import forms
from ftplib import MAXLINE
from .models import Exterior_payment

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(label = "descripcion de la tarea" , widget=forms.Textarea)
        
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
              field.widget.attrs['class'] = 'form-control'
              
          
          
        
        
class ExteriorPaymentForm(forms.ModelForm):
    """
    Form for creating an exterior payment request.

    Inherits from the Django ModelForm class and defines the fields to be displayed in the form.

    Attributes:
        Meta (class): Metadata class for the form.
        model (Exterior_payment): Django model associated with the form.
        fields (list): List of fields to be included in the form.

    Methods:
        __init__(self, *args, **kwargs): Initialize the form and add CSS classes to the form fields.
    """
    class Meta:
        model= Exterior_payment
        fields= ["beneficiary_name",
                 "beneficiary_last_name",
                 "beneficiary_document_type",
                 "beneficiary_document_no",
                 "passport_number",
                 "passport_expedition_city",
                 "address",
                 "bank_name",
                 "account_type",
                 "swift_code",
                 "iban_aba_code_type",
                 "iban_aba_code",
                 "account_name",
                 "account_number",
                 "bank_address"]
    
    """
    Constructor for the ExteriorPaymentForm class.

    Initializes the form and adds the 'form-control' class to all fields.

    Args:
        *args: Positional arguments.
        **kwargs: Named arguments.
    """    
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            field.widget.attrs['class'] = 'form-control'  
  
    

