from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from SistemaContableApp.models import Following, State, StateChange, Rol
from django.contrib.auth import get_user_model
from django.test import RequestFactory
from datetime import datetime
from django.utils import timezone

class HistoryStateTestCase(TestCase):

    def setUp(self):
        """
        Set up the necessary objects and data for the test case.

        This method is called before each individual test method is run.
        It creates a user with the role 'Administrador' and sets up a RequestFactory object.

        Args:
            self: The current instance of the test case.

        Returns:
            None
        """
        User = get_user_model()

        self.rol_Administrador = Rol.objects.create(rol='Administrador')       
        self.admin_user = User.objects.create_user(
            username='Admin',
            email='admin@gmail.com',
            name='Administrador',
            password='password'
        )
        self.admin_user.rol = self.rol_Administrador
        self.admin_user.save()

        self.factory = RequestFactory()


    def crear_instancia(self):
        """
        Creates an instance of the Following model with predefined values.

        Returns:
            None
        """
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
        """
        Test case to verify the initial state of the object Following.

        This test case logs in the admin user, creates an instance, and then checks that the initial state of the object
        Following is "Pendiente de aceptación". It uses the `assertEqual` method to compare the current state of the object
        with the expected state.
        """
        self.client.force_login(self.admin_user)
        self.crear_instancia()

        # Verificar que el estado inicial del objeto Following sea "Pendiente de aceptación"
        self.assertEqual(self.following.currentState, self.state_pending)

    def test_state_change(self):
        """
        Test case for changing the state of an object.

        This test case verifies that the state of an object is changed correctly from "Pendiente de aceptación" to "En revisión".
        It performs the following steps:
        1. Forces the client to log in as an admin user.
        2. Creates an instance of the object.
        3. Changes the state of the object to "En revisión".
        4. Verifies that the state has been changed correctly.

        """
        self.client.force_login(self.admin_user)
        self.crear_instancia()

        # Cambiar el estado de "Pendiente de aceptación" a "En revisión"
        self.following.currentState = self.state_review
        self.following.save()
        # Verificar que el estado se ha cambiado correctamente
        self.assertEqual(self.following.currentState, self.state_review)
            
    def test_state_change_history_display(self):
        """
        Test case for displaying state change history.

        This test case verifies that the state change history is correctly displayed
        when accessing the 'changeHistory' view with a specific following object.

        Steps:
        1. Force login as an admin user.
        2. Create an instance.
        3. Change the state of the following object to 'En revisión' and save.
        4. Access the 'changeHistory' view with the following object.
        5. Verify that the response status code is 200.
        6. Check if the following object and state changes are passed to the context.
        7. Verify the data of the first state change.

        Assertions:
        - The response status code should be 200.
        - The following object and state changes should be present in the context.
        - The data of the first state change should match the expected values.
        """
        self.client.force_login(self.admin_user)
        self.crear_instancia()

        # Change state and save
        state_review = State.objects.create(state="En revisión", color="orange")
        self.following.currentState = state_review
        self.following.save()

        # Access the view with the following object
        response = self.client.get(reverse('changeHistory', kwargs={'following_id': self.following.id}))
        self.assertEqual(response.status_code, 200)

        # Check if state changes are passed to the context
        self.assertIn('following', response.context)
        self.assertIn('state_changes', response.context)
        self.assertEqual(response.context['following'], self.following)
        self.assertEqual(len(response.context['state_changes']), 1)

        # Verify first state change data
        state_change = response.context['state_changes'][0]
        self.assertEqual(state_change.previousState, self.state_pending)
        self.assertEqual(state_change.currentState, state_review)

    
    def test_state_change_history_display(self):
        """
        Test case for displaying state change history.

        This test case verifies that the state change history is correctly displayed
        when accessing the 'changeHistory' view with a specific object.

        Steps:
        1. Force login as an admin user.
        2. Create an instance.
        3. Access the 'changeHistory' view with the object's ID.
        4. Verify that the response status code is 200.
        5. Check if the 'following' and 'state_changes' variables are passed to the context.
        6. Verify that the 'following' variable in the context is equal to the created instance.
        7. Verify that initially there are no state changes in the 'state_changes' variable.

        """
        self.client.force_login(self.admin_user)
        self.crear_instancia()

        # Access the view with the following object
        response = self.client.get(reverse('changeHistory', kwargs={'following_id': self.following.id}))
        self.assertEqual(response.status_code, 200)

        # Check if state changes are passed to the context
        self.assertIn('following', response.context)
        self.assertIn('state_changes', response.context)
        self.assertEqual(response.context['following'], self.following)
        
        # Verify no state changes initially
        self.assertEqual(len(response.context['state_changes']), 0)

