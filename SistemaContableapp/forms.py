from django import forms
from ftplib import MAXLINE
from .models import Charge_account, Requisition

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(label = "descripcion de la tarea" , widget=forms.Textarea)
        
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
              field.widget.attrs['class'] = 'form-control'
              
          
      
class DateInput(forms.DateInput):
    input_type = 'date'    
              
         
class ChargeAccountForm(forms.ModelForm):
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
    
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            field.widget.attrs['class'] = 'form-control'
            
            
class RequisitionForm(forms.ModelForm):
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
    
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            field.widget.attrs['class'] = 'form-control'
        
        
    
    
  
    

