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
        
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            field.widget.attrs['class'] = 'form-control'  
  
    

