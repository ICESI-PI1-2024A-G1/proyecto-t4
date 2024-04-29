from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from SistemaContableApp.models import Following, State, StateChange

class HistoryStateTestCase(TestCase):

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

    def test_state_change(self):
        # Cambiar el estado de "Pendiente de aceptación" a "En revisión"
        self.following.currentState = self.state_review
        self.following.save()
        # Verificar que el estado se ha cambiado correctamente
        self.assertEqual(self.following.currentState, self.state_review)
