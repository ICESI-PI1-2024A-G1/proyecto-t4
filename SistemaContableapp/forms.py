from django import forms
from ftplib import MAXLINE
from .models import *

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(label = "descripcion de la tarea" , widget=forms.Textarea)
        
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
              field.widget.attrs['class'] = 'form-control'
              
          
          
              
         
class ChargeAccountForm(forms.ModelForm):
    class Meta:
        model = Charge_account
        fields = ["name",
                  "identification",
                  "concept",
                  "value",
                  "retention_392_401",
                  "retention_383",
                  "declarant",
                  "colombian_resident",
                  "city",
                  "date",
                  "cex",
                  "bank",
                  "type",
                  "account_number"]
    
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            field.widget.attrs['class'] = 'form-control'
        

class ChargeAccountForm(forms.ModelForm):
    class Meta:
        model = Charge_account
        fields = ["name",
                  "identification",
                  "concept",
                  "value",
                  "retention_392_401",
                  "retention_383",
                  "declarant",
                  "colombian_resident",
                  "city",
                  "date",
                  "cex",
                  "bank",
                  "type",
                  "account_number"]
    
    def __init__(self, *args, **kwargs): # Adiciona 
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

