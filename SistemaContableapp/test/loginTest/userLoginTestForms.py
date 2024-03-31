from django.test import TestCase
from django.contrib.auth.models import User
from SistemaContableApp.forms import LoginForm, CustomUserCreationForm

class LoginFormTest(TestCase):
    def test_login_form_valid(self):
        """
        Test the login form with valid data.

        Verifies that the login form is valid when provided with valid data.
        """
        form_data = {'username': 'testuser', 'password': 'testpassword'}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_invalid(self):
        """
        Test the login form with invalid data.

        Verifies that the login form is invalid when provided with empty data.
        """
        form_data = {'username': '', 'password': ''}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())

class CustomUserCreationFormTest(TestCase):
    def test_custom_user_creation_form_valid(self):
        """
        Test the custom user creation form with valid data.

        Verifies that the custom user creation form is valid when provided with valid data.
        """
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
        """
        Test the custom user creation form with invalid data.

        Verifies that the custom user creation form is invalid when provided with mismatched passwords or empty data.
        """
        # Test with mismatched passwords
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password1': 'testpassword',
            'password2': 'differentpassword'
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

        # Test with empty data
        form_data = {}
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
