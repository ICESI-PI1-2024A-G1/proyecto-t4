from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from SistemaContableApp.models import  *
from SistemaContableApp.views import  *

class UserModelTestCase(TestCase):
    def setUp(self):
        self.rol_admin = Rol.objects.create(rol='Administrador')
        self.rol_solicitante = Rol.objects.create(rol='Solicitante')
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            name='Test',
            password='testpassword'
        )
    
    def test_user_creation(self):
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_user_str_representation(self):
        self.assertEqual(str(self.user), 'Test, None')

    def test_user_rol_assignment(self):
        self.user.rol = self.rol_admin
        self.user.save()
        self.assertEqual(self.user.rol, self.rol_admin)

class UserUpdateFormTestCase(TestCase):
    def setUp(self):
        self.rol_admin = Rol.objects.create(rol='Administrador')
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            name='Test',
            password='testpassword'
        )

    def test_user_update_form_valid(self):
        form_data = {
            'email': 'newemail@example.com',
            'name': 'New Name',
            'last_name': 'New Last Name',
            'rol': self.rol_admin.id,
        }
        form = UserUpdateForm(data=form_data, instance=self.user)
        self.assertTrue(form.is_valid())

    def test_user_update_form_invalid(self):
        form_data = {
            'email': 'invalidemail',
            'name': 'New Name',
            'last_name': 'New Last Name',
            'rol': self.rol_admin.id,
        }
        form = UserUpdateForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())

class UserViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.rol_admin = Rol.objects.create(rol='Administrador')
        self.user_admin = User.objects.create_user(
            username='admin',
            email='admin@example.com',
            name='Admin',
            password='adminpassword'
        )
        self.user_admin.rol= self.rol_admin
        self.user_admin.save()

    def test_user_list_view(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_list.html')

    def test_edit_user_view_get(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('edit_user', args=[self.user_admin.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_user.html')

    def test_edit_user_view_post(self):
        self.client.login(username='admin', password='adminpassword')
        form_data = {
            'email': 'newemail@example.com',
            'name': 'New Name',
            'last_name': 'New Last Name',
            'rol': self.rol_admin.id,
        }
        response = self.client.post(reverse('edit_user', args=[self.user_admin.id]), data=form_data)
        self.assertRedirects(response, reverse('user_list'))

    def test_delete_user_view_get(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('delete_user', args=[self.user_admin.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'confirm_delete_user.html')

    def test_delete_user_view_post(self):
        self.client.login(username='admin', password='adminpassword')
        response = self.client.post(reverse('delete_user', args=[self.user_admin.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(id=self.user_admin.id).exists())