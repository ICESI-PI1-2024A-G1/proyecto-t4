from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from SistemaContableApp.models import Following, State, Rol


class StatesTestCase(TestCase):
    
    def setUp(self):
        """
        Set up the necessary objects and configurations for the test case.

        This method is called before each test method is executed.

        It creates two user objects: an admin user and a gestor user, using the Django's User model.
        The admin user has the username 'Admin', email 'admin@gmail.com', name 'Administrador', and password 'password'.
        The gestor user has the username 'Gestor', email 'gestor@gmail.com', name 'Gestor', and password 'password'.

        It also creates a Django test client object for making HTTP requests.

        This method is automatically called by the testing framework.
        """
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
        """
        Creates instances of State and Following models with the given parameters.

        Args:
            acceptance_state (str): The acceptance state of the following.
            revision_state (str): The revision state of the following.
            approval_state (str): The approval state of the following.

        Returns:
            None
        """
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
        """
        Test case to verify the acceptance state update when the user is authenticated.
        """
        self.client.force_login(self.admin_user)
        
        self.crear_instancias(acceptance_state='Aceptado')  # Estado inicial 'Pendiente'
        
        url = reverse('acceptance_state', args=[self.following.id])
        data = {'acceptance_state': 'Aceptado'}
        response = self.client.post(url, data, follow=True)  # Agrega follow=True
        self.following.refresh_from_db()
        self.assertEqual(response.status_code, 200)  # Código de estado 200 OK
        self.assertEqual(self.following.acceptanceState, 'Aceptado')

    def test_acceptance_state_authenticated_rejected(self):
        """
        Test case to verify the behavior of accepting a state as an authenticated user and setting it to 'Rechazado'.
        """
        self.client.force_login(self.admin_user)
        self.crear_instancias(acceptance_state='Rechazado')
        url = reverse('acceptance_state', args=[self.following.id])
        data = {'acceptance_state': 'Rechazado'}
        response = self.client.post(url, data, follow=True)  # Agrega follow=True
        self.following.refresh_from_db()
        self.assertEqual(response.status_code, 200)  # Código de estado 200 OK
        self.assertEqual(self.following.acceptanceState, 'Rechazado')


    def test_set_revision_state_authenticated(self):
        """
        Test case to verify the behavior of setting the revision state when the user is authenticated.
        """
        self.client.force_login(self.admin_user)
        self.crear_instancias(revision_state='En revisión')  
        url = reverse('revision_state', args=[self.following.id])
        data = {'revision_state': 'En revisión'}
        response = self.client.post(url, data, follow=True)
        self.following.refresh_from_db()
        self.assertEqual(response.status_code, 200)  # Código de estado 200 OK
        self.assertEqual(self.following.revisionState, 'En revisión')

    def test_set_invalid_revision_state(self):
        """
        Test case to verify that an invalid revision state is not allowed to be set.

        This test case performs the following steps:
        1. Forces the client to log in as an admin user.
        2. Creates instances with a None revision state.
        3. Constructs the URL for the 'revision_state' view, passing the ID of the 'following' object as an argument.
        4. Sets the data dictionary with an invalid revision state that exceeds 10 characters.
        5. Sends a POST request to the URL with the data.
        6. Refreshes the 'following' object from the database.
        7. Asserts that the response status code is 200 (OK).
        8. Asserts that the revision state of the 'following' object has not changed (remains None).
        """
        self.client.force_login(self.admin_user)
        self.crear_instancias(revision_state=None)  
        url = reverse('revision_state', args=[self.following.id])
        data = {'revision_state': 'Aceptado por profesionales, que test tan largos'}  # Intentar establecer un estado no permitido, es decir con más de 10 caracteres
        response = self.client.post(url, data, follow=True)
        self.following.refresh_from_db()
        self.assertEqual(response.status_code, 200)  # Código de estado 200 OK
        self.assertIsNone(self.following.revisionState)  # El estado de revisión no debería haber cambiado
    
    def test_set_approval_state_authenticated(self):
        """
        Test case to verify the behavior of setting the approval state when the user is authenticated.
        """
        self.client.force_login(self.admin_user)
        self.crear_instancias(approval_state='Aprobado')  # Estado inicial None
        url = reverse('approval_state', args=[self.following.id])
        data = {'approval_state': 'Aprobado'}
        response = self.client.post(url, data, follow=True)
        self.following.refresh_from_db()
        self.assertEqual(response.status_code, 200)  # Código de estado 200 OK
        self.assertEqual(self.following.approvalState, 'Aprobado')

    def test_set_invalid_approval_state(self):
        """
        Test case to verify that an invalid approval state cannot be set.

        This test case ensures that when an invalid approval state (with more than ten characters) is attempted to be set,
        the state should not be changed and the response status code should be 200 OK.

        Steps:
        1. Force login as an admin user.
        2. Create instances with initial approval state as None.
        3. Generate the URL for setting the approval state for a specific instance.
        4. Set the data with an invalid approval state (more than ten characters).
        5. Send a POST request to the URL with the data.
        6. Refresh the instance from the database.
        7. Assert that the response status code is 200 OK.
        8. Assert that the approval state of the instance is still None.

        """
        self.client.force_login(self.admin_user)
        self.crear_instancias(approval_state=None)  # Estado inicial None
        url = reverse('approval_state', args=[self.following.id])
        data = {'approval_state': 'En revisión, es de arduo trabajo trabajar'}  # Intentar establecer un estado no permitido, es decir con más de diez caracteres
        response = self.client.post(url, data, follow=True)
        self.following.refresh_from_db()
        self.assertEqual(response.status_code, 200)  # Código de estado 200 OK
        self.assertIsNone(self.following.approvalState)  # El estado de aprobación no debería haber cambiado