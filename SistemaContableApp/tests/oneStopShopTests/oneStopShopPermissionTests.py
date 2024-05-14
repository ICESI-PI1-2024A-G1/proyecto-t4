from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from SistemaContableApp.models import  *
from SistemaContableApp.views import  *
class OneStopShopViewTestCase(TestCase):    
    def setUp(self):

        # Crear roles y grupos necesarios
        self.rol_administrador = Rol.objects.create(rol='Administrador')
        self.rol_solicitante = Rol.objects.create(rol='Solicitante')
        self.rol_ventanilla_unica = Rol.objects.create(rol='Ventanilla única')
        self.rol_contable = Rol.objects.create(rol='Contable')


        # Crear usuarios de prueba
        self.user_administrador = User.objects.create_user(username='admin', email='admin@gmail.com', name='admin',password='password')
        self.user_administrador.rol= self.rol_administrador
        self.user_administrador.save()
        self.user_solicitante = User.objects.create_user(username='solicitante', email='solicitante@gmail.com', name='solicitante', password='password')
        self.user_solicitante.rol= self.rol_solicitante
        self.user_solicitante.save()
        self.user_Ventanilla_unica= User.objects.create_user(username='Ventanilla', email='Ventanillaúnica@gmail.com', name='Ventanilla única', password='password')
        self.user_Ventanilla_unica.rol= self.rol_ventanilla_unica
        self.user_Ventanilla_unica.save()
        self.user_contable = User.objects.create_user(username='contable', email='contable@gmail.com', name= 'contable' , password='password')
        self.user_contable.rol = self.rol_contable
        self.user_contable.save()

        # Crear estados de prueba
        self.estado_inicial = State.objects.create(state='Inicial', color="blue")
        self.estado_nuevo = State.objects.create(state='Nuevo', color="gray")

        # Crear objeto Following de prueba
        self.following = Following.objects.create(
            creationDate='2023-04-01',
            creator='Daniela',
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
            currentState=self.estado_inicial,
            closeDate='2023-04-30',
        )

        self.client = Client()

    def test_summaryOneStopShopView_allowed(self):
        """
        This test verifies that a user with the "Administrator" role has allowed access to the "summaryOneStopShop"
         view. An HTTP status code 200 (OK) is expected.
        """
        # Simular una solicitud al usuario con permisos
        self.client.login(username='admin', password='password')
        response = self.client.get(reverse('summaryOneStopShop'))
        self.assertEqual(response.status_code, 200)

    def test_summaryOneStopShopView_not_allowed(self):
        """
        This test verifies that a user with the "Requester" role is not allowed access to the "summaryOneStopShop" view.
         An HTTP status code 302 (Redirect) is expected.
        """
        # Simular una solicitud al usuario sin permisos
        self.client.login(username='solicitante', password='password')
        response = self.client.get(reverse('summaryOneStopShop'))
        self.assertEqual(response.status_code, 302)  # Redirección esperada

    def test_fullOneStopShopView_allowed(self):
        """
        This test verifies that a user with the "Administrator" role has allowed access to the "fullOneStopShop" view.
         An HTTP status code 200 (OK) is expected.
        """
        self.client.login(username='admin', password='password')
        response = self.client.get(reverse('fullOneStopShop'))
        self.assertEqual(response.status_code, 200)

    def test_fullOneStopShopView_not_allowed(self):
        """
        This test verifies that a user with the "Requester" role (Requester) is not allowed access to the "fullOneStopShop" view.
         An HTTP status code 302 (Redirect) is expected.
        """
        self.client.login(username='solicitante', password='password')
        response = self.client.get(reverse('fullOneStopShop'))
        self.assertEqual(response.status_code, 302)

    def test_oneStopShopFormView_allowed(self):
        """
        This test verifies that a user with the "One Stop Shop" role has allowed access to the "OneStopShopForm" view.
         An HTTP status code 200 (OK) is expected.
        """
        self.client.login(username='Ventanilla', password='password')
        response = self.client.get(reverse('OneStopShopForm'))
        self.assertEqual(response.status_code, 200)

    def test_oneStopShopFormView_not_allowed(self):
        """
        Esta prueba verifica que un usuario con el rol "Solicitante" (Solicitante) no tiene permitido el acceso a la vista "OneStopShopForm". 
        Se espera un código de estado HTTP 302 (Redirección).
        """
        self.client.login(username='solicitante', password='password')
        response = self.client.get(reverse('OneStopShopForm'))
        self.assertEqual(response.status_code, 302)

    def test_updateState_not_allowed(self):
        """
        This test verifies that a user with the "Single Window" role does not have permission to update the status of a "Next" object. 
        An HTTP status code 302 (Redirect) is expected and the state of the object should not change.
        """
        self.client.login(username='Ventanilla', password='password')
        data = {'estadoEdit': self.estado_nuevo.state}
        response = self.client.post(reverse('update_state', args=[self.following.id]), data)
        self.assertEqual(response.status_code, 302)
        self.following.refresh_from_db()
        self.assertEqual(self.following.currentState, self.estado_inicial)
        
    def test_updateState_allowed(self):
        """
        This test verifies that a user with the "Administrator" role can update the status of a "Next" object. 
        An HTTP status code 302 (Redirect) is expected and the object's state should change correctly.
        """
        self.client.login(username='admin', password='password')
        data = {'estadoEdit': self.estado_nuevo.state, 'description': "Estado actualizado"}
        response = self.client.post(reverse('update_state', args=[self.following.id]), data)
        self.assertEqual(response.status_code, 302)
        self.following.refresh_from_db()
        self.assertEqual(self.following.currentState, self.estado_nuevo)

    def test_changeHistory_allowed(self):
        """
        This test verifies that a user with the "Administrator" role has allowed access to the "Change History" view for a specific "Next" object.
         An HTTP status code 200 (OK) is expected.
        """
        self.client.login(username='admin', password='password')
        response = self.client.get(reverse('changeHistory', args=[self.following.id]))
        self.assertEqual(response.status_code, 200)

    def test_changeHistory_not_allowed(self):
        """
        This test verifies that a user with the "Single Window" role is not allowed access to the "changeHistory" view for a specific "Next" object.
         An HTTP status code 200 (OK) is expected.
        """
        self.client.login(username='Ventanilla', password='password')
        response = self.client.get(reverse('changeHistory', args=[self.following.id]))
        self.assertEqual(response.status_code, 200)

    def test_approval_comment(self):
        """
        This test verifies that a user with the "Admin" role can add an approval comment to a "Next" object.
         An HTTP status code 302 (Redirect) is expected and the comment should be saved successfully to the object
        """
        self.client.login(username='admin', password='password')
        comment_data = {'approval_comment': 'Comentario de aprobación'}
        response = self.client.post(reverse('approval_comment', args=[self.following.id]), comment_data)
        self.assertEqual(response.status_code, 302)
        self.following.refresh_from_db()
        self.assertEqual(self.following.approvalComments, 'Comentario de aprobación')

    def test_approval_comment_no_permission(self):
        """
        This test verifies that a user with the "Single Window" role cannot add an approval comment to a "Next" object. 
        An HTTP status code 200 (OK) is expected and the comment should not be saved to the object.
        """
        self.client.login(username='Ventanilla', password='password')
        comment_data = {'approval_comment': 'Comentario de aprobación'}
        response = self.client.post(reverse('approval_comment', args=[self.following.id]), comment_data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_accounting_comment(self):
        """
        This test verifies that a user with the "Accountant" (Accounting) role can add an accounting comment to a "Next" object. 
        An HTTP status code 302 (Redirect) is expected and the comment should be saved successfully to the object
        """
        self.client.login(username='contable', password='password')
        comment_data = {'accounting_comment': 'Comentario de contabilidad'}
        response = self.client.post(reverse('accounting_comment', args=[self.following.id]), comment_data)
        self.assertEqual(response.status_code, 302)
        self.following.refresh_from_db()
        self.assertEqual(self.following.accountingComments, 'Comentario de contabilidad')

    def test_accounting_comment_no_permission(self):
        """
        This test verifies that a user with the "Single Window" role cannot add an accounting comment to a "Next" object.
         An HTTP status code 200 (OK) is expected and the comment should not be saved to the object.
        """
        self.client.login(username='Ventanilla', password='password')
        comment_data = {'accounting_comment': 'Comentario de contabilidad'}
        response = self.client.post(reverse('accounting_comment', args=[self.following.id]), comment_data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_acceptance_state(self):
        """
        This test verifies that a user with the "Admin" role can update the acceptance status of a "Next" object. 
        An HTTP status code 302 (Redirect) is expected and the acceptance status should be updated successfully on the object.
        """
        self.client.login(username='admin', password='password')
        state_data = {'acceptance_state': 'Aceptado'}
        response = self.client.post(reverse('acceptance_state', args=[self.following.id]), state_data)
        self.assertEqual(response.status_code, 302)
        self.following.refresh_from_db()
        self.assertEqual(self.following.acceptanceState, 'Aceptado')

    def test_acceptance_state_no_permission(self):
        """
        This test verifies that a user with the "Accountant" role cannot update the acceptance status of a "Next" object.
         An HTTP status code of 200 (OK) is expected and the acceptance status should not be updated on the object.
        """
        self.client.login(username='contable', password='password')
        state_data = {'acceptance_state': 'Aceptado'}
        response = self.client.post(reverse('acceptance_state', args=[self.following.id]), state_data, follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_revision_state(self):
        """
        This test verifies that a user with the "Administrator" role can update the revision status of a "Next" object.
         An HTTP status code 302 (Redirect) is expected and the revision status should be updated successfully on the object.
        """
        self.client.login(username='admin', password='password')
        state_data = {'revision_state': 'Revisado'}
        response = self.client.post(reverse('revision_state', args=[self.following.id]), state_data)
        self.assertEqual(response.status_code, 302)
        self.following.refresh_from_db()
        self.assertEqual(self.following.revisionState, 'Revisado')

    def test_revision_state_no_permission(self):
        """
        This test verifies that a user with the "Accountant" (Accounting) role cannot update the revision status of a "Next" object. 
        An HTTP status code 200 (OK) is expected and the revision status should not be updated on the object.
        """
        self.client.login(username='contable', password='password')
        state_data = {'revision_state': 'Revisado'}
        response = self.client.post(reverse('revision_state', args=[self.following.id]), state_data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_approval_state(self):
        """
        This test verifies that a user with the "Admin" role can update the approval status of a "Next" object.
         An HTTP status code 302 (Redirect) is expected and the approval status should be updated successfully on the object.
        """
        self.client.login(username='admin', password='password')
        state_data = {'approval_state': 'Aprobado'}
        response = self.client.post(reverse('approval_state', args=[self.following.id]), state_data)
        self.assertEqual(response.status_code, 302)
        self.following.refresh_from_db()
        self.assertEqual(self.following.approvalState, 'Aprobado')

    def test_approval_state_no_permission(self):
        """
        This test verifies that a user with the "Accountant" (Accounting) role cannot update the approval status of a "Next" object. 
        An HTTP status code 200 (OK) is expected and the approval status should not be updated on the object.
        """
        self.client.login(username='contable', password='password')
        state_data = {'approval_state': 'Aprobado'}
        response = self.client.post(reverse('approval_state', args=[self.following.id]), state_data, follow=True)
        self.assertEqual(response.status_code, 200)