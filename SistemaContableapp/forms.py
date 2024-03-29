from django import forms
from ftplib import MAXLINE
from .models import Charge_account, Requisition
        

class DateInput(forms.DateInput):
    """
    Class that defines a date input field.
    Extends the forms.DateInput class from Django.
    Attributes:
        input_type (str): The type of input field. In this case, 'date'.
    """
    
    input_type = 'date'    

              

  
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
        
        
    
    
  
    

