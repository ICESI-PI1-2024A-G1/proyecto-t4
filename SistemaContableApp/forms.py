from django import forms
from ftplib import MAXLINE
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from .models import *
from django.forms import inlineformset_factory
from django.forms import BaseInlineFormSet
        

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
                  "colombian_resident",
                  "supports"
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
              
              

class TravelExpensesSolicitationForm(forms.ModelForm):
    class Meta:
        model = Legalization
        fields = ["legalization_date",
                  "traveler_name",
                  "identification",
                  "cost_center",
                  "dependency",
                  "destiny_city",
                  "travel_date",
                  "return_date",
                  "motive",
                  "bank",
                  "type_account",
                  "account_number",
                  "orderer_name",
                  "elaborator_name",
                  "descount_in_one_quote",
                  "advance_payment_value",
                  "currency_type_of_advance_value"]
        
        widgets = {
            'legalization_date': DateInput(),
            'travel_date': DateInput(),
            'return_date': DateInput(),
            
        }
        
    def __init__(self, *args, **kwargs):
        """
        Constructor for the TravelExpensesSolicitationForm class.

        Initializes the form and adds the 'form-control' class to all fields.

        Args:
            *args: Positional arguments.
            **kwargs: Named arguments.
        """
        
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            field.widget.attrs['class'] = 'form-control'

class TravelExpenseForm(forms.ModelForm):
    class Meta:
        model = LegalizationExpense
        fields = ['category',
                  'support',
                  'support_no',
                  'third_person_name',
                  'third_person_nit',
                  'concept',
                  'money_type',
                  'money_value']

class TravelExpensesSolicitationFormSet(forms.BaseInlineFormSet):
   
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in self.fields.items():   
              field.widget.attrs['class'] = 'form-control'
            
TravelExpenseFormSet = inlineformset_factory(
    Legalization, LegalizationExpense,
    fields=['category',
            'support',
            'support_no',
            'third_person_name',
            'third_person_nit',
            'concept',
            'money_type',
            'money_value'],
    extra=0,
)     


class LegalizationExpenseInlineFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fk = LegalizationExpense._meta.get_field('solicitation')





class TravelAdvanceSolicitationForm(forms.ModelForm):
    class Meta:
        model = AdvancePayment
        fields = ["radicate",
                  "payment_order_code",
                  "request_date",
                  "traveler_name",
                  "traveler_id",
                  "cost_center",
                  "dependency",
                  "destiny_city",
                  "travel_date",
                  "return_date",
                  "motive",
                  "currency_type_of_advance_value",
                  "last_day_in_icesi",
                  "descount_in_one_quote",
                  "orderer_name",
                  "elaborator_name"]
        
        widgets = {
            'request_date': DateInput(),
            'travel_date': DateInput(),
            'return_date': DateInput(),
            'last_day_in_icesi' : DateInput(),
            
        }
        
    def __init__(self, *args, **kwargs):
        """
        Constructor for the TravelAdvanceSolicitationForm class.

        Initializes the form and adds the 'form-control' class to all fields.

        Args:
            *args: Positional arguments.
            **kwargs: Named arguments.
        """
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            field.widget.attrs['class'] = 'form-control'


class TravelAdvanceExpenseForm(forms.ModelForm):
    class Meta:
        model = AdvanceExpense
        fields=['category',
                'money_value']

class TravelAdvanceExpensesSolicitationFormSet(forms.BaseInlineFormSet):
   
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)  
        for field in self.fields.items():   
              field.widget.attrs['class'] = 'form-control'
            
TravelAdvanceExpenseFormSet = inlineformset_factory(
    AdvancePayment, AdvanceExpense,
    fields=['category',
            'money_value'],
    extra=0,
)     

class AdvanceExpenseInlineFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fk = AdvanceExpense._meta.get_field('solicitation')    
     
     
     
     
     
     
     
     
              

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget= forms.PasswordInput)

class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(label = "Nombre",max_length=30, required=True)
    last_name = forms.CharField(label ="Apellidos",max_length=30, required=True)
    email = forms.EmailField(label = "Correo Electrónico",max_length=254, help_text='Required. Inform a valid email address.')
    password1 = forms.CharField(label="Contraseña", strip=False, widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", strip=False, widget=forms.PasswordInput, help_text='Enter the same password as before, for verification.')

    class Meta:
        model = User
        fields = ('name', 'last_name', 'email', 'password1', 'password2', 'rol')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    rol = forms.ModelChoiceField(queryset=Rol.objects.all(), required=False)

    class Meta:
        model = User
        fields = ['email', 'name', 'last_name', 'rol']



        
class OneStopShopForm(forms.ModelForm):

    """
    Form class for the one-stop shop data entry.

    Extends the forms.ModelForm class from Django.

    Attributes:
    - Meta: Specifies the model and fields to be used in the form.

    Model:
    - Following: Model for storing data related to following objects.
    """

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
    
    """
    Form class for attaching documents to the one-stop shop.

    Extends the forms.ModelForm class from Django.
    
    Attributes:
    - Meta: Specifies the model and fields to be used in the form.

    Model:
    - AttachedDocument: Model for storing data related to attached documents.

    Fields:
    - file: File field for uploading documents.
    """

    class Meta:
        model = AttachedDocument
        fields = ['file']