from django import forms
from ftplib import MAXLINE
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(label = "descripcion de la tarea" , widget=forms.Textarea)
        
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
              field.widget.attrs['class'] = 'form-control'

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget= forms.PasswordInput)

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label = "Nombre",max_length=30, required=True)
    last_name = forms.CharField(label ="Apellido",max_length=30, required=True)
    email = forms.EmailField(label = "Correo-Outlook",max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    
    
  
    

