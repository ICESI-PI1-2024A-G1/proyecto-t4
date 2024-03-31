from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class UserRequestViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
     
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_forgot_password_view(self):
    
        response = self.client.get(reverse('olvidar_contraseña'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_form.html')

    def test_user_login_view(self):
     
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_registration_view(self):
       
        response = self.client.get(reverse('registration'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/registro.html')

    def test_password_reset_request_view(self):
       
        response = self.client.get(reverse('password_reset'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/password_reset_form.html')

    def test_successful_user_login(self):  
    
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        response = self.client.post(reverse('login'), {'email': 'test@example.com', 'password': 'password'})
        self.assertRedirects(response, reverse('index'))

    def test_successful_password_reset_request(self):
   
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
        response = self.client.post(reverse('password_reset'), {'email': 'test@example.com'})
        self.assertRedirects(response, reverse('password_reset_done'))
