from django.test import TestCase
from django.contrib.auth.models import User
from SistemaContableApp.forms import LoginForm, CustomUserCreationForm

class LoginFormTest(TestCase):
    def test_login_form_valid(self):
        
        form_data = {'username': 'testuser', 'password': 'testpassword'}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_invalid(self):
       
        form_data = {'username': '', 'password': ''}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())

class CustomUserCreationFormTest(TestCase):
    def test_custom_user_creation_form_valid(self):
       
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_custom_user_creation_form_invalid(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password1': 'testpassword',
            'password2': 'differentpassword'
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        form_data = {}
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
