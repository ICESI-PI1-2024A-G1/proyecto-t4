from django import forms
from ftplib import MAXLINE
from .models import *
        

class DateInput(forms.DateInput):
    """
    Class that defines a date input field.
    Extends the forms.DateInput class from Django.
    Attributes:
        input_type (str): The type of input field. In this case, 'date'.
    """
    
    input_type = 'date'    

              
          
          
        
        
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
  
class ChargeAccountForm(forms.ModelForm):
    """
    Form to create a charge account request.

    Extends the forms.ModelForm class from Django.

    Attributes:
        Meta (class): Meta class that defines the fields and associated model.
    """
    
    class Meta:
        model = Charge_account
        fields = ["name",
                  "identification",
                  "phone",
                  "city",
                  "addres",
                  "date",
                  "value_letters",
                  "value_numbers",
                  "concept",
                  "bank",
                  "type",
                  "account_number",
                  "cex",
                  "retentions",
                  "declarant",
                  "colombian_resident"
                  ]
        widgets = {
            'date': DateInput()
        }
    
    def __init__(self, *args, **kwargs):
        """
        Constructor for the ChargeAccountForm class.

        Initializes the form and adds the 'form-control' class to all fields.

        Args:
            *args: Positional arguments.
            **kwargs: Named arguments.
        """
        
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            field.widget.attrs['class'] = 'form-control'
        

class RequisitionForm(forms.ModelForm):
    """
    Form to create a requisition request.

    Extends the forms.ModelForm class from Django.

    Attributes:
        Meta (class): Meta class that defines the fields and associated model.
    """
    
    class Meta:
        model = Requisition
        fields = ["date",
                  "beneficiaryName",
                  "idNumber",
                  "charge",
                  "dependency",
                  "cenco",
                  "value",
                  "concept",
                  "description",
                  "radicate",
                  "payment_order_code",
                  "paymentMethod",
                  "typeAccount",
                  "account_number",
                  "authorName"
                  ]
        widgets = {
            'date': DateInput()
        }
    
    def __init__(self, *args, **kwargs):
        """
        Constructor for the RequisitionForm class.

        Initializes the form and adds the 'form-control' class to all fields.

        Args:
            *args: Positional arguments.
            **kwargs: Named arguments.
        """
        
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            field.widget.attrs['class'] = 'form-control' 

        
class OneStopShopForm(forms.ModelForm):
    class Meta:
        model = Following
        fields = [ "creationDate",
                  "creator",
                  "type",
                  "supplier",
                  "supplierId",
                  "documentNumber",
                  "concept",
                  "supplierEmail",
                  "moneyType",
                  "amount",
                  "cenco",
                  "cexNumber",
                  "observations",
                  "currentState",
                  "closeDate"]

class AttachedDocumentForm(forms.ModelForm):
    class Meta:
        model = AttachedDocument
        fields = ['file']