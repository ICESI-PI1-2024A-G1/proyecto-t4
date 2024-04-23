from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from SistemaContableApp.models import Following, State

class ModifyStateTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')
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
        # Preparar datos de prueba
        new_state = State.objects.create(state="Nuevo Estado", color="blue")

        # Obtener la URL para la vista update_state con el ID del following
        url = reverse('update_state', args=[self.following.id])

        # Enviar una solicitud POST a la vista con el nuevo estado
        response = self.client.post(url, {'estadoEdit': new_state.state})

        # Verificar que la vista redirige correctamente después de la actualización
        self.assertRedirects(response, reverse('fullOneStopShop'))

        # Actualizar el estado del following en la base de datos
        self.following.refresh_from_db()

        # Verificar que el estado se actualizó correctamente
        self.assertEqual(self.following.currentState, new_state)

    def test_update_state_view_invalid_state(self):
        # Obtener la URL para la vista update_state con el ID del following
        url = reverse('update_state', args=[self.following.id])

        # Enviar una solicitud POST a la vista con un estado inválido
        response = self.client.post(url, {'estadoEdit': 'Estado Inválido'})

        # Verificar que la vista redirige a la página correcta
        self.assertRedirects(response, reverse('fullOneStopShop'))

        # Verificar que el estado del following no ha cambiado
        self.following.refresh_from_db()
        self.assertEqual(self.following.currentState, self.state)
