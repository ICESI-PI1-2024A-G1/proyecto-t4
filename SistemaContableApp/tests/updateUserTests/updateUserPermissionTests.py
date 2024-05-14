from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from SistemaContableApp.models import  *
from SistemaContableApp.views import  *

a
class updateUserPermissionTestCase(TestCase):

    def setUp(self):
   
        # Crear roles y grupos necesarios
        self.rol_administrador = Rol.objects.create(rol='Administrador')
        self.rol_solicitante = Rol.objects.create(rol='Solicitante')


        # Crear usuarios de prueba
        self.user_administrador = User.objects.create_user(username='admin', email='admin@gmail.com', name='admin',password='password')
        self.user_administrador.rol= self.rol_administrador
        self.user_administrador.save()

        self.user_solicitante = User.objects.create_user(username='solicitante', email='solicitante@gmail.com', name='solicitante', password='password')
        self.user_solicitante.rol= self.rol_solicitante
        self.user_solicitante.save()

        self.client = Client()

    def test_user_list_allowed(self):
        """
        Tests if a user with the 'Administrador' role has permission to access the 'user_list' view.
        Logs in with the administrator user, makes a GET request to the 'user_list' view,
        and verifies that the HTTP status code is 200 (OK).
        """
        self.client.login(username='admin', password='password')
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)

    def test_user_list_not_allowed(self):
        """
        Tests if a user with the 'Solicitante' role does not have permission to access the 'user_list' view.
        Logs in with the applicant user, makes a GET request to the 'user_list' view,
        and verifies that the HTTP status code is 302 (Redirection).
        """
        self.client.login(username='solicitante', password='password')
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 302)

    def test_edit_user_allowed(self):
        """
        Tests if a user with the 'Administrador' role has permission to access the 'edit_user' view.
        Logs in with the administrator user, makes a GET request to the 'edit_user' view with the administrator user's ID,
        and verifies that the HTTP status code is 200 (OK).
        """
        self.client.login(username='admin', password='password')
        response = self.client.get(reverse('edit_user', args=[self.user_administrador.id]))
        self.assertEqual(response.status_code, 200)

    def test_edit_user_not_allowed(self):
        """
        Tests if a user with the 'Solicitante' role does not have permission to access the 'edit_user' view.
        Logs in with the applicant user, makes a GET request to the 'edit_user' view with the administrator user's ID,
        and verifies that the HTTP status code is 302 (Redirection).
        """
        self.client.login(username='solicitante', password='password')
        response = self.client.get(reverse('edit_user', args=[self.user_administrador.id]))
        self.assertEqual(response.status_code, 302)

    def test_delete_user_allowed(self):
        """
        Tests if a user with the 'Administrador' role has permission to access the 'delete_user' view.
        Logs in with the administrator user, makes a GET request to the 'delete_user' view with the administrator user's ID,
        and verifies that the HTTP status code is 200 (OK).
        """
        self.client.login(username='admin', password='password')
        response = self.client.get(reverse('delete_user', args=[self.user_administrador.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_user_not_allowed(self):
        """
        Tests if a user with the 'Solicitante' role does not have permission to access the 'delete_user' view.
        Logs in with the applicant user, makes a GET request to the 'delete_user' view with the administrator user's ID,
        and verifies that the HTTP status code is 302 (Redirection).
        """
        self.client.login(username='solicitante', password='password')
        response = self.client.get(reverse('delete_user', args=[self.user_administrador.id]))
        self.assertEqual(response.status_code, 302)