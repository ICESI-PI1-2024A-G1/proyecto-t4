from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from SistemaContableApp.models import Following, State, StateChange

class ModifyStateTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')
        self.state_pending = State.objects.create(state="Pendiente de aceptación", color="gray")
        self.state_review = State.objects.create(state="En revisión", color="orange")
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
            currentState=self.state_pending,
            closeDate='2023-04-30',
        )
    
           
    def test_initial_state(self):
        # Verificar que el estado inicial del objeto Following sea "Pendiente de aceptación"
        self.assertEqual(self.following.currentState, self.state_pending)


    def test_state_change_history(self):
        # Verificar que no hay cambios de estado al principio
        self.assertEqual(StateChange.objects.count(), 0)

        # Cambiar el estado del objeto Following y verificar el historial
        response = self.client.post(reverse('update_state', args=[self.following.id]), {'estadoEdit': 'En revisión'})
        self.assertEqual(response.status_code, 302)  # Redireccionamiento exitoso

        # Verificar que se ha creado un registro en el historial de cambios de estado
        self.assertEqual(StateChange.objects.count(), 1)

        # Verificar que el estado cambiado sea correcto
        state_change = StateChange.objects.first()
        self.assertEqual(state_change.following, self.following)
        self.assertEqual(state_change.state, self.state_review)

    def test_state_change_permission(self):
        # Verificar que un usuario no autenticado no puede cambiar el estado
        self.client.logout()
        response = self.client.post(reverse('update_state', args=[self.following.id]), {'estadoEdit': 'En revisión'})
        self.assertEqual(response.status_code, 302)  # Redireccionamiento a la página de inicio de sesión
