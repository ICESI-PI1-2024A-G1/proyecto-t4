from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from SistemaContableApp.models import Following, State, Rol
from django.test import RequestFactory
from django.contrib.messages import get_messages

class ModifyStateTestCase(TestCase):
    def setUp(self):
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
        # Crear un usuario sin el rol de administrador
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
