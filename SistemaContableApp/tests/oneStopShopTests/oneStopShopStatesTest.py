from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from SistemaContableApp.models import Following, State, Rol


class StatesTestCase(TestCase):
    
    def setUp(self):
        User = get_user_model()
        self.admin_user = User.objects.create_user(
            username='Admin',
            email='admin@gmail.com',
            name='Administrador',
            password='password'
        )
        self.gestor_user = User.objects.create_user(
            username='Gestor',
            email='gestor@gmail.com',
            name='Gestor',
            password='password'
        )
        self.factory = Client()

    def crear_instancias(self, acceptance_state=None, revision_state=None, approval_state=None):
        self.state = State.objects.create(state="Pendiente de aceptación", color="gray")
        self.following = Following.objects.create(
            creationDate='2023-04-01',
            creator='John Paul',
            type='Solicitud',
            supplier='Dinero SAS.',
            supplierId='12345',
            documentNumber='DOC001',
            manager='Jane Smith',
            acceptor='Alice Brown',
            revisor='Bob Smith',
            acceptanceState=acceptance_state,
            acceptanceDate=None,
            revisionState=revision_state,
            revision=None,
            concept='Compra de suministros',
            supplierEmail='dinero@example.com',
            moneyType='USD',
            amount=1000,
            cenco='CENCO1',
            cexNumber='CEX001',
            observations='Ninguna',
            revisionDate=None,
            approvalState=approval_state,
            approval=None,
            approvalDate=None,
            approvalComments=None,
            accountingReception=None,
            accountingComments=None,
            accountingDate=None,
            receptor=None,
            modificationDate=None,
            modifier=None,
            currentState=self.state,
            closeDate='2023-04-30',
        )


    def test_acceptance_state_authenticated(self):
        self.client.force_login(self.admin_user)
        
        self.crear_instancias(acceptance_state='Aceptado')  # Estado inicial 'Pendiente'
        
        url = reverse('acceptance_state', args=[self.following.id])
        data = {'acceptance_state': 'Aceptado'}
        response = self.client.post(url, data, follow=True)  # Agrega follow=True
        self.following.refresh_from_db()
        self.assertEqual(response.status_code, 200)  # Código de estado 200 OK
        self.assertEqual(self.following.acceptanceState, 'Aceptado')

    def test_acceptance_state_authenticated_rejected(self):
        self.client.force_login(self.admin_user)
        self.crear_instancias(acceptance_state='Rechazado')
        url = reverse('acceptance_state', args=[self.following.id])
        data = {'acceptance_state': 'Rechazado'}
        response = self.client.post(url, data, follow=True)  # Agrega follow=True
        self.following.refresh_from_db()
        self.assertEqual(response.status_code, 200)  # Código de estado 200 OK
        self.assertEqual(self.following.acceptanceState, 'Rechazado')


    def test_set_revision_state_authenticated(self):
        self.client.force_login(self.admin_user)
        self.crear_instancias(revision_state='En revisión')  
        url = reverse('revision_state', args=[self.following.id])
        data = {'revision_state': 'En revisión'}
        response = self.client.post(url, data, follow=True)
        self.following.refresh_from_db()
        self.assertEqual(response.status_code, 200)  # Código de estado 200 OK
        self.assertEqual(self.following.revisionState, 'En revisión')

    def test_set_invalid_revision_state(self):
        self.client.force_login(self.admin_user)
        self.crear_instancias(revision_state=None)  
        url = reverse('revision_state', args=[self.following.id])
        data = {'revision_state': 'Aceptado por profesionales, que test tan largos'}  # Intentar establecer un estado no permitido, es decir con más de 10 caracteres
        response = self.client.post(url, data, follow=True)
        self.following.refresh_from_db()
        self.assertEqual(response.status_code, 200)  # Código de estado 200 OK
        self.assertIsNone(self.following.revisionState)  # El estado de revisión no debería haber cambiado
    
    def test_set_approval_state_authenticated(self):
        self.client.force_login(self.admin_user)
        self.crear_instancias(approval_state='Aprobado')  # Estado inicial None
        url = reverse('approval_state', args=[self.following.id])
        data = {'approval_state': 'Aprobado'}
        response = self.client.post(url, data, follow=True)
        self.following.refresh_from_db()
        self.assertEqual(response.status_code, 200)  # Código de estado 200 OK
        self.assertEqual(self.following.approvalState, 'Aprobado')

    def test_set_invalid_approval_state(self):
        self.client.force_login(self.admin_user)
        self.crear_instancias(approval_state=None)  # Estado inicial None
        url = reverse('approval_state', args=[self.following.id])
        data = {'approval_state': 'En revisión, es de arduo trabajo trabajar'}  # Intentar establecer un estado no permitido, es decir con más de diez caracteres
        response = self.client.post(url, data, follow=True)
        self.following.refresh_from_db()
        self.assertEqual(response.status_code, 200)  # Código de estado 200 OK
        self.assertIsNone(self.following.approvalState)  # El estado de aprobación no debería haber cambiado