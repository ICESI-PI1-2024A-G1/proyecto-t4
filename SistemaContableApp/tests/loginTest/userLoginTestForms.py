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
            'name': 'John',
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
            'name': 'John',
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

class LoginFormAdditionalTest(TestCase):
    def test_login_form_valid_additional(self):
        """
        Test the login form with additional valid data.

        Verifies that the login form is valid when provided with additional valid data.
        """
        form_data = {'username': 'testuser', 'password': 'testpassword'}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_invalid_additional(self):
        """
        Test the login form with additional invalid data.

        Verifies that the login form is invalid when provided with additional empty data.
        """
        form_data = {'username': '', 'password': ''}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())

class CustomUserCreationFormAdditionalTest(TestCase):
    def test_custom_user_creation_form_valid_additional(self):
        """
        Test the custom user creation form with additional valid data.

        Verifies that the custom user creation form is valid when provided with additional valid data.
        """
        form_data = {
            'name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_custom_user_creation_form_invalid_additional(self):
        """
        Test the custom user creation form with additional invalid data.

        Verifies that the custom user creation form is invalid when provided with additional mismatched passwords or empty data.
        """
        # Test with mismatched passwords
        form_data = {
            'name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password1': 'testpassword',
            'password2': 'differentpassword'
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

        # Test with additional empty data
        form_data = {}
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        def test_login_form_valid_new(self):
         """
            Test the login form with valid data.

             Verifies that the login form is valid when provided with valid data.
        """
        form_data = {'username': 'testuser', 'password': 'testpassword'}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_invalid_new(self):
        """
        Test the login form with invalid data.

        Verifies that the login form is invalid when provided with empty data.
        """
        form_data = {'username': '', 'password': ''}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())

class CustomUserCreationFormTestsNew(TestCase):
    def test_custom_user_creation_form_valid_new(self):
        """
        Test the custom user creation form with valid data.

        Verifies that the custom user creation form is valid when provided with valid data.
        """
        form_data = {
            'name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_custom_user_creation_form_invalid_new(self):
        """
        Test the custom user creation form with invalid data.

        Verifies that the custom user creation form is invalid when provided with mismatched passwords or empty data.
        """
        # Test with mismatched passwords
        form_data = {
            'name': 'John',
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

class LoginFormExtraTestsNew(TestCase):
    def test_login_form_valid_extra_new(self):
        """
        Test the login form with additional valid data.

        Verifies that the login form is valid when provided with additional valid data.
        """
        form_data = {'username': 'testuser', 'password': 'testpassword'}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_invalid_extra_new(self):
        """
        Test the login form with additional invalid data.

        Verifies that the login form is invalid when provided with additional empty data.
        """
        form_data = {'username': '', 'password': ''}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())

class CustomUserCreationFormExtraTestsNew(TestCase):
    def test_custom_user_creation_form_valid_extra_new(self):
        """
        Test the custom user creation form with additional valid data.

        Verifies that the custom user creation form is valid when provided with additional valid data.
        """
        form_data = {
            'name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_custom_user_creation_form_invalid_extra_new(self):
        """
        Test the custom user creation form with additional invalid data.

        Verifies that the custom user creation form is invalid when provided with additional mismatched passwords or empty data.
        """
        # Test with mismatched passwords
        form_data = {
            'name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password1': 'testpassword',
            'password2': 'differentpassword'
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

        # Test with additional empty data
        form_data = {}
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        def test_login_form_valid_extra(self):
         """
         Test the login form with additional valid data.

         Verifies that the login form is valid when provided with additional valid data.
            """
        form_data = {'username': 'testuser', 'password': 'testpassword'}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_invalid_extra(self):
        """
        Test the login form with additional invalid data.

        Verifies that the login form is invalid when provided with additional empty data.
        """
        form_data = {'username': '', 'password': ''}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())

class CustomUserCreationFormTestsExtra(TestCase):
    def test_custom_user_creation_form_valid_extra(self):
        """
        Test the custom user creation form with additional valid data.

        Verifies that the custom user creation form is valid when provided with additional valid data.
        """
        form_data = {
            'name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_custom_user_creation_form_invalid_extra(self):
        """
        Test the custom user creation form with additional invalid data.

        Verifies that the custom user creation form is invalid when provided with additional mismatched passwords or empty data.
        """
        # Test with mismatched passwords
        form_data = {
            'name': 'John',
            'last_name': 'Doe',
            'email': 'johndoe@example.com',
            'password1': 'testpassword',
            'password2': 'differentpassword'
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

        # Test with additional empty data
        form_data = {}
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

class LoginFormSpecialTests(TestCase):
    def test_login_form_valid_special(self):
        """
        Test the login form with special valid data.

        Verifies that the login form is valid when provided with special valid data.
        """
        form_data = {'username': 'testuser', 'password': 'testpassword'}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_invalid_special(self):
        """
        Test the login form with special invalid data.

        Verifies that the login form is invalid when provided with special empty data.
        """
        form_data = {'username': '', 'password': ''}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
    