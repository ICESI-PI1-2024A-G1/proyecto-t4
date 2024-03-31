from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class UserRequestViewsTest(TestCase):
    def setUp(self):
        """
        Set up the test environment.
        """
        self.client = Client()

    def test_index_view(self):
        """
        Test the index view.

        Verifies that the index view returns a status code of 200 and uses the correct template.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_forgot_password_view(self):
        """
        Test the forgot password view.

        Verifies that the forgot password view returns a status code of 200 and uses the correct template.
        """
        response = self.client.get(reverse('olvidar_contraseña'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_form.html')

    def test_user_login_view(self):
        """
        Test the user login view.

        Verifies that the user login view returns a status code of 200 and uses the correct template.
        """
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_registration_view(self):
        """
        Test the registration view.

        Verifies that the registration view returns a status code of 200 and uses the correct template.
        """
        response = self.client.get(reverse('registration'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/registro.html')

    def test_password_reset_request_view(self):
        """
        Test the password reset request view.

        Verifies that the password reset request view returns a status code of 200 and uses the correct template.
        """
        response = self.client.get(reverse('password_reset'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_form.html')

    def test_successful_user_login(self):  
        """
        Test successful user login.

        Verifies that a user can successfully log in.
        """
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        response = self.client.post(reverse('login'), {'email': 'test@example.com', 'password': 'password'})
        self.assertRedirects(response, reverse('index'))

    def test_successful_password_reset_request(self):
        """
        Test successful password reset request.

        Verifies that a user can successfully request a password reset.
        """
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        response = self.client.post(reverse('password_reset'), {'email': 'test@example.com'})
        self.assertRedirects(response, reverse('password_reset_done'))