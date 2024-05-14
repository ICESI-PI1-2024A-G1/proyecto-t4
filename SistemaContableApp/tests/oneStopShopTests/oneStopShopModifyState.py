from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from SistemaContableApp.models import Following, State, Rol
from django.test import RequestFactory
from django.contrib.messages import get_messages

class ModifyStateTestCase(TestCase):
    def setUp(self):
        """
        Set up the test case by creating necessary objects and data.
        """
        User = get_user_model()
        self.rol_Adminstrador = Rol.objects.create(rol='Administrador')
        self.admin_user = User.objects.create_user(
            username='Admin',
            email='admin@gmail.com',
            name='Administrador',
            password='password'
        )
        self.admin_user.rol = self.rol_Adminstrador
        self.admin_user.save()
        self.factory = RequestFactory()
   

    def crear_instancia(self):
        """
        Creates an instance of `Following` and `State` objects.

        Returns:
            None
        """
        self.state = State.objects.create(state="Pendiente de aceptación", color="gray")
        self.following = Following.objects.create(
            creationDate='2023-04-01',
            creator='John Doe',
            type='Solicitud',
            supplier='Acme Inc.',
            supplierId='12345',
            documentNumber='DOC001',
            manager='Jane Smith',
            concept='Compra de suministros',
            moneyType='USD',
            amount=1000,
            cenco='CENCO1',
            cexNumber='CEX001',
            observations='Ninguna',
            currentState=self.state,
            closeDate='2023-04-30',
        )

    def test_update_state_view(self):
        """
        Test case for updating the state view.

        This test case verifies that the state view is updated correctly when a new state is selected
        for a following object. It performs the following steps:
        1. Forces the client to log in as an admin user.
        2. Creates an instance of the following object.
        3. Creates a new state object.
        4. Retrieves the URL for the update_state view with the ID of the following object.
        5. Sends a POST request to the view with the new state and a description.
        6. Verifies that the view redirects correctly after the update.
        7. Refreshes the state of the following object from the database.
        8. Verifies that the state was updated correctly.

        """
        self.client.force_login(self.admin_user)

        self.crear_instancia()
        new_state = State.objects.create(state="Nuevo Estado", color="blue")
        # Obtener la URL para la vista update_state con el ID del following
        url = reverse('update_state', args=[self.following.id])
        # Enviar una solicitud POST a la vista con el nuevo estado
        response = self.client.post(url, {'estadoEdit': new_state.state, 'description': 'Cambio importante'})
        # Verificar que la vista redirige correctamente después de la actualización
        self.assertRedirects(response, reverse('fullOneStopShop'))
        # Refrescar el estado del following desde la base de datos
        self.following.refresh_from_db()
        # Verificar que el estado se actualizó correctamente
        self.assertEqual(self.following.currentState, new_state)

    def test_update_state_view_invalid_state(self):
        """
        Test case to verify the behavior of the update_state view when an invalid state is provided.

        Steps:
        1. Force login as an admin user.
        2. Create an instance.
        3. Get the URL for the update_state view with the ID of the following.
        4. Send a POST request to the view with an invalid state.
        5. Verify that the view redirects to the correct page.
        6. Refresh the state of the following from the database.
        7. Verify that the state of the following has not changed.

        """
        self.client.force_login(self.admin_user)

        self.crear_instancia()
        # Obtener la URL para la vista update_state con el ID del following
        url = reverse('update_state', args=[self.following.id])
        # Enviar una solicitud POST a la vista con un estado inválido
        response = self.client.post(url, {'estadoEdit': 'Estado Inválido'})
        # Verificar que la vista redirige a la página correcta
        self.assertRedirects(response, reverse('fullOneStopShop'))
        # Refrescar el estado del following desde la base de datos
        self.following.refresh_from_db()
        # Verificar que el estado del following no ha cambiado
        self.assertEqual(self.following.currentState, self.state)
    
    def test_update_state_to_current_state(self):
        """
        Test case to verify that updating the state to the current state does not change the following's state.

        Steps:
        1. Force login as an admin user.
        2. Create an instance.
        3. Get the URL for the update_state view with the ID of the following.
        4. Send a POST request to the view with the same current state.
        5. Verify that the view redirects to the correct page.
        6. Refresh the following's state from the database.
        7. Verify that the following's state has not changed.
        """

        self.client.force_login(self.admin_user)
        self.crear_instancia()

        # Obtener la URL para la vista update_state con el ID del following
        url = reverse('update_state', args=[self.following.id])

        # Enviar una solicitud POST a la vista con el mismo estado actual
        response = self.client.post(url, {'estadoEdit': self.state.state, 'description': 'No cambio'})

        # Verificar que la vista redirige a la página correcta
        self.assertRedirects(response, reverse('fullOneStopShop'))

        # Refrescar el estado del following desde la base de datos
        self.following.refresh_from_db()

        # Verificar que el estado del following no ha cambiado
        self.assertEqual(self.following.currentState, self.state)
    
    def test_update_state_unauthorized_user(self):
        """
        Test case to verify that an unauthorized user cannot update the state of a following.

        Steps:
        1. Create a regular user without the administrator role.
        2. Log in the regular user.
        3. Create an instance.
        4. Create a new state.
        5. Get the URL for the update_state view with the ID of the following.
        6. Send a POST request to the view with the new state.
        7. Check the error message in the response.
        8. Refresh the state of the following from the database.
        9. Verify that the state of the following has not changed.

        """
        User = get_user_model()
        regular_user = User.objects.create_user(
            username='regular',
            email='regular@example.com',  # Agrega el correo electrónico requerido
            name='Regular User',  # Agrega el nombre requerido
            password='password'
        )
        self.client.force_login(regular_user)
        self.crear_instancia()
        new_state = State.objects.create(state="Nuevo Estado", color="blue")

        # Obtener la URL para la vista update_state con el ID del following
        url = reverse('update_state', args=[self.following.id])

        # Enviar una solicitud POST a la vista con el nuevo estado
        response = self.client.post(url, {'estadoEdit': new_state.state, 'description': 'Cambio no autorizado'})

        # Obtener los mensajes de error de la respuesta
        messages = list(get_messages(response.wsgi_request))

        # Verificar que se muestra el mensaje de error de permisos
        self.assertEqual(str(messages[0]), 'No tienes los permisos requeridos')

        # Refrescar el estado del following desde la base de datos
        self.following.refresh_from_db()

        # Verificar que el estado del following no ha cambiado
        self.assertEqual(self.following.currentState, self.state)
