from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from SistemaContableApp.models import  *
from SistemaContableApp.views import  *
a
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
        """
        This test verifies that a new user is created correctly in the database. 
        Checks that a User object with the user name 'testuser' exists.
        """
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_user_str_representation(self):
        """
        This test verifies that the text string representation of the User object is correct. 
        Check that when converting the User object created in the setUp to a string, the expected value 'Test, None' is obtained.
        """
        self.assertEqual(str(self.user), 'Test, None')

    def test_user_rol_assignment(self):
        """
        This test verifies that a role can be correctly assigned to a user.
         Assign the 'Administrator' role to the user created in the setup and check that the assigned role is the same.
        """
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
        """
        This test verifies that the UserUpdateForm form is valid with correct data. 
        Create a dictionary with valid data, create an instance of the form with that data and the user instance created in setUp, and check that the form is valid.
        """
        form_data = {
            'email': 'newemail@example.com',
            'name': 'New Name',
            'last_name': 'New Last Name',
            'rol': self.rol_admin.id,
        }
        form = UserUpdateForm(data=form_data, instance=self.user)
        self.assertTrue(form.is_valid())

    def test_user_update_form_invalid(self):
        """
        This test verifies that the UserUpdateForm form is invalid with incorrect data. Create a dictionary with an invalid data (incorrect email),
         create an instance of the form with that data and the user instance created in the setUp, and check that the form is invalid.
        """
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
        """
        This test verifies that an admin user can access the user list view. Simulates a GET request to the 'user_list' view with an authenticated admin user,
         and verifies that an HTTP status code of 200 (OK) is returned and that the 'user_list.html' template is used.
        """
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_list.html')

    def test_edit_user_view_get(self):
        """
        This test verifies that an admin user can access a particular user's edit view. Mock a GET request to the 'edit_user' view with an authenticated admin user, 
        and check that an HTTP status code of 200 (OK) is returned and that the 'update_user.html' template is used.
        """
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('edit_user', args=[self.user_admin.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'update_user.html')

    def test_edit_user_view_post(self):
        """
        This test verifies that an admin user can update data for a particular user. 
        Mock a POST request to the 'edit_user' view with valid form data and an authenticated admin user, and check that it is redirected to the 'user_list' view.
        """
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
        """
        This test verifies that an admin user can access the confirmation view to delete a particular user. Mock a GET request to the 'delete_user' view with an authenticated admin user,
         and check that an HTTP status code of 200 (OK) is returned and that the 'confirm_delete_user.html' template is used.
        """
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('delete_user', args=[self.user_admin.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'confirm_delete_user.html')

    def test_delete_user_view_post(self):
        """
        This test verifies that an admin user can delete a particular user. Simulate a POST request to the 'delete_user' view with an authenticated administrator user, 
        and verify that an HTTP status code 302 (redirect) is obtained and that the User object corresponding to the administrator user created in the setUp no longer exists in the database. data.
        """
        self.client.login(username='admin', password='adminpassword')
        response = self.client.post(reverse('delete_user', args=[self.user_admin.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(id=self.user_admin.id).exists())