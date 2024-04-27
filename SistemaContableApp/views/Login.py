from SistemaContableApp.models import  *
from SistemaContableApp.forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import render, redirect   
from django.contrib import messages



def index(request):
    """
    View for the home page.

    Displays the home page of the accounting system.

    Args:
        request (HttpRequest): The received HTTP request.

    Returns:
        HttpResponse: The HTTP response rendering the home page.
  
    """
    
    title = "¡Bienvenidos al Sistema Contable"
    return render(request,'index.html', {
        'title' : title 
    })


def olvidar_contraseña(request):
    """
    View for the forgot password page.

    Displays the forgot password page.

    Args:
        request (HttpRequest): The received HTTP request.

    Returns:
        HttpResponse: The HTTP response rendering the forgot password page.
    """
    return render(request,'registration/password_reset_form.html' )


def user_login(request):
    """
    View for user login.

    Processes the login form and authenticates the user.

    Args:
        request (HttpRequest): The received HTTP request.

    Returns:
        HttpResponse: Redirects to the home page if login is successful, 
                      otherwise redirects to the login page.
    """
   
    if request.method == 'POST':
        email = request.POST.get('email')  
        password = request.POST.get('password')
        user = authenticate(request,
                            username=request.POST['email'],
                            password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(index)  
            else:
                messages.error(request, 'El usuario no está activo')
                return redirect('index') 
        else:
            messages.error(request, 'No tienes una cuenta, por favor registrate')
            return redirect('index') 
    else:
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})          
           
@login_required
def dashboard(request):
    return render(request,'index.html')
    

def registration(request):
        """
        View for user registration.

        Processes the user registration form and creates a new user account.

        Args:
            request (HttpRequest): The received HTTP request.

        Returns:
            HttpResponse: Redirects to the home page if registration is successful,
                        otherwise redirects to the registration page.
        """
        
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                messages.success(request, 'Tu cuenta ha sido creada exitosamente.')
                login(request, user)
                messages.success(request, 'Registro exitoso.')
                return redirect('index')
            else:
                messages.error(request, 'Error en el registro. Por favor, revise los datos introducidos.')
        else:
            form = CustomUserCreationForm()
        return render(request, 'registration/registrationUsers.html', {'form': form})

def password_reset_request(request):
    """
    View for requesting a password reset.

    Processes the password reset request form and sends an email with instructions
    to reset the password.

    Args:
        request (HttpRequest): The received HTTP request.

    Returns:
        HttpResponse: Redirects to the password reset done page if the request is
                      successful, otherwise renders the password reset form page.
    """
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            # Django's password reset form already includes functionality to send the email
            password_reset_form.save(
                request=request,
                use_https=False,
                email_template_name='registration/password_reset_email.html',
            )
            return redirect('password_reset_done')
    else:
        password_reset_form = PasswordResetForm()
    return render(request, 'registration/password_reset_form.html', {'form': password_reset_form})