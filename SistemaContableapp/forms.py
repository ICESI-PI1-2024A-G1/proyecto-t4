from django import forms
from ftplib import MAXLINE
from .models import CollectionAccount

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(label = "descripcion de la tarea" , widget=forms.Textarea)
        
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
              field.widget.attrs['class'] = 'form-control'
              
          
          
              
         
class CollectionAccountForm(forms.ModelForm):
    class Meta:
        model = CollectionAccount
        fields = ["remitente",
                  "nombre",
                  "identificacion",
                  "sumadeValorEnLetras",
                  "sumadeValorEnNumeros",
                  "concepto",
                  "ciudadYFecha",
                  "direccion",
                  "nombreDelBanco",
                  "tipoDeCuenta",
                  "NoDeCuenta",
                  "cexNo"]
    
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            field.widget.attrs['class'] = 'form-control'
        
    
  
    

