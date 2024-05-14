from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from SistemaContableApp.models import Following, State, Rol
from django.test import RequestFactory

class CommentsTestCase(TestCase):

    def setUp(self):
        """
        Set up the necessary objects and data for the test case.

        This method is called before each individual test method is run.
        It creates and saves instances of User and Rol models with different roles.
        It also creates a RequestFactory object for generating test requests.
        """
        User = get_user_model()
        self.rol_Administrador = Rol.objects.create(rol='Administrador')
        self.rol_Gestor = Rol.objects.create(rol='Gestor')
        self.rol_Contable = Rol.objects.create(rol='Contable')
        self.rol_Ventanilla_unica = Rol.objects.create(rol='Ventanilla única')

        self.admin_user = User.objects.create_user(
            username='Admin',
            email='admin@gmail.com',
            name='Administrador',
            password='password'
        )
        self.admin_user.rol = self.rol_Administrador
        self.admin_user.save()

        self.gestor_user = User.objects.create_user(
            username='Gestor',
            email='gestor@gmail.com',
            name='Gestor',
            password='password'
        )
        self.gestor_user.rol = self.rol_Gestor
        self.gestor_user.save()

        self.contable_user = User.objects.create_user(
            username='Contable',
            email='contable@gmail.com',
            name='Contable',
            password='password'
        )
        self.contable_user.rol = self.rol_Contable
        self.contable_user.save()

        self.ventanilla_unica_user = User.objects.create_user(
            username='Ventanilla',
            email='ventanilla@gmail.com',
            name='Ventanilla única',
            password='password'
        )
        self.ventanilla_unica_user.rol = self.rol_Ventanilla_unica
        self.ventanilla_unica_user.save()

        self.factory = RequestFactory()

    def crear_instancia(self):
        """
        Creates an instance of Following with the specified attributes.

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
            concept='Compra de suministros',
            moneyType='USD',
            amount=1000,
            cenco='CENCO1',
            cexNumber='CEX001',
            observations='Ninguna',
            currentState=self.state,
            closeDate='2023-04-30',
        )

    def test_approval_comment_unauthorized(self):
        """
        Test case to verify that an unauthorized user cannot approve a comment.
        """
        self.client.force_login(self.admin_user)

        self.crear_instancia()
        url = reverse('approval_comment', args=[self.following.id])
        response = self.client.post(url, {'approval_comment': 'Comentario de prueba'})
        self.assertEqual(response.status_code, 302)  # Redireccionado a la página de inicio de sesión

    def test_approval_comment_empty(self):
        """
        Test case to verify the behavior when the approval comment is empty.

        This test logs in the admin user, creates an instance, and then sends a POST request to the 'approval_comment' endpoint
        with an empty approval comment. It then checks if the 'approvalComments' attribute of the 'following' object is empty.
        """
        self.client.force_login(self.admin_user)

        self.crear_instancia()
        url = reverse('approval_comment', args=[self.following.id])
        response = self.client.post(url, {'approval_comment': ''})
        self.following.refresh_from_db()
        self.assertEqual(self.following.approvalComments, '')

    def test_approval_comment_valid(self):
        """
        Test case to verify the functionality of approving a comment.

        This test case logs in an admin user, creates an instance, and then posts an approval comment.
        It checks if the approval comment is successfully saved in the database.
        """
        self.client.force_login(self.admin_user)

        self.crear_instancia()
        url = reverse('approval_comment', args=[self.following.id])
        comment_text = 'Comentario de aprobación'
        response = self.client.post(url, {'approval_comment': comment_text})
        self.following.refresh_from_db()
        self.assertEqual(self.following.approvalComments, comment_text)

    def test_approval_comment_redirect(self):
        """
        Test case for checking the redirection after submitting an approval comment.

        This test logs in an admin user, creates an instance, and then posts an approval comment.
        It verifies that the response is redirected to the 'fullOneStopShop' page and there are no success messages.
        """
        self.client.force_login(self.admin_user)

        self.crear_instancia()
        url = reverse('approval_comment', args=[self.following.id])
        response = self.client.post(url, {'approval_comment': 'Comentario de prueba'}, follow=True)
        self.assertRedirects(response, reverse('fullOneStopShop'))
        messages = list(response.context.get('messages'))
        self.assertEqual(len(messages), 0)  # No hay mensajes de éxito

    def test_approval_comment_not_allowed(self):
        """
        Test case to verify that ventanilla unica is not allowed to post an approval comment.

        Steps:
        1. Log in as the ventanilla_unica_user.
        2. Create an instance.
        3. Post an approval comment with invalid content.
        4. Verify that the response is a redirect with status code 302.
        5. Follow the redirect and get the redirected response.
        6. Verify that the redirected response has a status code of 200.
        7. Verify that the content of the redirected response matches the expected error message.

        """
        self.client.force_login(self.ventanilla_unica_user)
        self.crear_instancia()

        url = reverse('approval_comment', args=[self.following.id])
        response = self.client.post(url, {'approval_comment': 'Comentario no válido'})

        # Verificar que la respuesta es un código de estado 302 (Redireccionado)
        self.assertEqual(response.status_code, 302)

        # Obtener la redirección y seguir
        redirected_url = response.url
        redirected_response = self.client.get(redirected_url)

        # Verificar que la respuesta de la redirección es un código de estado 200 (Éxito)
        self.assertEqual(redirected_response.status_code, 200)

        # Verificar que el contenido de la respuesta coincide con el mensaje esperado
        expected_html = '<div class="modal-content">\n<span class="close">×</span>\n<h2>Error!</h2>\n<p>No tienes los permisos requeridos</p>\n<button id="btnOk">OK</button>\n</div>'
        self.assertContains(redirected_response, expected_html, html=True)

    def test_accounting_comment_valid_admin(self):
        """
        Test case to verify that an accounting comment can be added by an admin user.

        Steps:
        1. Force login as an admin user.
        2. Create an instance.
        3. Get the URL for the accounting comment view.
        4. Set the comment text.
        5. Send a POST request to the URL with the comment text.
        6. Refresh the instance from the database.
        7. Assert that the accounting comment is equal to the comment text.
        """
        self.client.force_login(self.admin_user)
        self.crear_instancia()
        url = reverse('accounting_comment', args=[self.following.id])
        comment_text = 'Comentario de contabilidad'
        response = self.client.post(url, {'accounting_comment': comment_text})
        self.following.refresh_from_db()
        self.assertEqual(self.following.accountingComments, comment_text)

    def test_accounting_comment_valid_gestor(self):
        """
        Test case to verify that a valid accounting comment can be added by a gestor user.
        """
        self.client.force_login(self.gestor_user)
        self.crear_instancia()
        url = reverse('accounting_comment', args=[self.following.id])
        comment_text = 'Comentario de contabilidad'
        response = self.client.post(url, {'accounting_comment': comment_text})
        self.following.refresh_from_db()
        self.assertEqual(self.following.accountingComments, comment_text)

    def test_accounting_comment_valid_contable(self):
        """
        Test case for validating accounting comment by a 'contable' user.

        This test case verifies that a 'contable' user can successfully create an accounting comment
        for a specific instance. It checks if the comment is correctly saved in the database.

        Steps:
        1. Force login as a 'contable' user.
        2. Create an instance.
        3. Generate the URL for the 'accounting_comment' view.
        4. Set the comment text.
        5. Send a POST request to the 'accounting_comment' view with the comment data.
        6. Refresh the instance from the database.
        7. Assert that the accounting comment of the instance matches the comment text.

        """
        self.client.force_login(self.contable_user)
        self.crear_instancia()
        url = reverse('accounting_comment', args=[self.following.id])
        comment_text = 'Comentario de contabilidad'
        response = self.client.post(url, {'accounting_comment': comment_text})
        self.following.refresh_from_db()
        self.assertEqual(self.following.accountingComments, comment_text)

    def test_accounting_comment_invalid_user(self):
        """
        Test case to verify that an invalid user cannot post an accounting comment.

        Steps:
        1. Force login as the ventanilla_unica_user.
        2. Create an instance.
        3. Generate the URL for the accounting_comment view with the following.id as argument.
        4. Set the comment_text to 'Comentario no válido'.
        5. Send a POST request to the URL with the accounting_comment data.
        6. Verify that the response status code is 302 (Redirection).
        7. Get the redirected URL and send a GET request to it.
        8. Verify that the redirected response status code is 200 (Success).
        9. Verify that the redirected response contains the expected HTML content.
        """
        self.client.force_login(self.ventanilla_unica_user)
        self.crear_instancia()
        url = reverse('accounting_comment', args=[self.following.id])
        comment_text = 'Comentario no válido'
        response = self.client.post(url, {'accounting_comment': comment_text})
        # Verificar que la respuesta es un código de estado 302 (Redireccionado)
        self.assertEqual(response.status_code, 302)
        # Obtener la redirección y seguir
        redirected_url = response.url
        redirected_response = self.client.get(redirected_url)
        # Verificar que la respuesta de la redirección es un código de estado 200 (Éxito)
        self.assertEqual(redirected_response.status_code, 200)
        # Verificar que el contenido de la respuesta coincide con el mensaje esperado
        expected_html = '<div class="modal-content">\n<span class="close">×</span>\n<h2>Error!</h2>\n<p>No tienes los permisos requeridos</p>\n<button id="btnOk">OK</button>\n</div>'
        self.assertContains(redirected_response, expected_html, html=True)

    def test_accounting_comment_redirect(self):
        """
        Test case for the accounting_comment view redirect.

        This test ensures that when a user submits an accounting comment, 
        they are redirected to the fullOneStopShop view.

        Steps:
        1. Force login as an admin user.
        2. Create an instance.
        3. Generate the URL for the accounting_comment view.
        4. Set the comment text.
        5. Send a POST request to the URL with the comment text.
        6. Assert that the response redirects to the fullOneStopShop view.
        7. Check that there are no success messages in the response context.
        """
        self.client.force_login(self.admin_user)
        self.crear_instancia()
        url = reverse('accounting_comment', args=[self.following.id])
        comment_text = 'Comentario de contabilidad'
        response = self.client.post(url, {'accounting_comment': comment_text}, follow=True)
        self.assertRedirects(response, reverse('fullOneStopShop'))
        messages = list(response.context.get('messages'))
        self.assertEqual(len(messages), 0)  # No hay mensajes de éxito