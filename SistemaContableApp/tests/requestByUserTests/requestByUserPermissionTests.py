from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from SistemaContableApp.models import  *
from SistemaContableApp.views import  *
from datetime import datetime, date

class FormCreationViewTestCaseP(TestCase):
    def setUp(self):
   
        # Crear roles y grupos necesarios
        self.rol_administrador = Rol.objects.create(rol='Administrador')
        self.rol_solicitante = Rol.objects.create(rol='Solicitante')
        self.rol_contable = Rol.objects.create(rol='Contable')


        # Crear usuarios de prueba
        self.user_administrador = User.objects.create_user(username='admin', email='admin@gmail.com', name='admin',password='password')
        self.user_administrador.rol= self.rol_administrador
        self.user_administrador.save()

        self.user_solicitante = User.objects.create_user(username='solicitante', email='solicitante@gmail.com', name='solicitante', password='password')
        self.user_solicitante.rol= self.rol_solicitante
        self.user_solicitante.save()

        self.user_contable = User.objects.create_user(username='contable', email='contable@gmail.com', name= 'contable' , password='password')
        self.user_contable.rol = self.rol_contable
        self.user_contable.save()

        self.client = Client()

    def test_createChargeAccountForm_allowed(self):
        """
        This test verifies that a user with the "Requester" role has permission to access the "viewChargeAccountForm" view.
        Wait for an HTTP status code of 200 (OK).
        It also checks if the form instance in the context is of type ChargeAccountForm.
        """
        self.client.login(username='solicitante', password='password')
        response = self.client.get(reverse('viewChargeAccountForm'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], ChargeAccountForm)

    def test_createChargeAccountForm_not_allowed(self):
        """
        This test verifies that a user with the "Accountant" role does not have permission to access the "viewChargeAccountForm" view.
        Expect an HTTP status code of 302 (Redirect).
        """
        self.client.login(username='contable', password='password')
        response = self.client.get(reverse('viewChargeAccountForm'))
        self.assertEqual(response.status_code, 302)

    def test_createRequisitionForm_allowed(self):
        """
        This test verifies that a user with the "Requisitioner" role has permission to access the "viewRequisitionForm" view.
        Wait for an HTTP status code of 200 (OK).
        It also checks if the form instance in the context is of type RequisitionForm.
        """
        self.client.login(username='solicitante', password='password')
        response = self.client.get(reverse('viewRequisitionForm'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], RequisitionForm)

    def test_createRequisitionForm_not_allowed(self):
        """
        This test verifies that a user with the "Accountant" role does not have permission to access the "viewRequisitionForm" view.
        Expect an HTTP status code of 302 (Redirect).
        """
        self.client.login(username='contable', password='password')
        response = self.client.get(reverse('viewRequisitionForm'))
        self.assertEqual(response.status_code, 302) 

    def test_createExteriorPaymentForm_allowed(self):
        """
        This test verifies that a user with the "Applicant" role has permission to access the "viewExteriorPaymentForm" view.
        Wait for an HTTP status code of 200 (OK).
        It also checks if the form instance in the context is of type ExteriorPaymentForm.
        """
        self.client.login(username='solicitante', password='password')
        response = self.client.get(reverse('viewExteriorPaymentForm'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], ExteriorPaymentForm)

    def test_createExteriorPaymentForm_not_allowed(self):
        """
        This test verifies that a user with the "Accountant" role does not have permission to access the "viewExteriorPaymentForm" view.
        Expect an HTTP status code of 302 (Redirect).
        """
        self.client.login(username='contable', password='password')
        response = self.client.get(reverse('viewExteriorPaymentForm'))
        self.assertEqual(response.status_code, 302)

    def test_createLegalizationForm_allowed(self):
        """
        This test verifies that a user with the "Applicant" role has permission to access the "viewLegalizationForm" view.
        Wait for an HTTP status code of 200 (OK).
        It also checks if the form instance in the context is of type TravelExpensesSolicitationForm.
        """
        self.client.login(username='solicitante', password='password')
        response = self.client.get(reverse('viewLegalizationForm'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['solicitation_form'], TravelExpensesSolicitationForm)

    def test_createLegalizationForm_not_allowed(self):
        """
        This test verifies that a user with the "Accountant" role does not have permission to access the "viewLegalizationForm" view.
        Expect an HTTP status code of 302 (Redirect).
        """
        self.client.login(username='contable', password='password')
        response = self.client.get(reverse('viewLegalizationForm'))
        self.assertEqual(response.status_code, 302)

    def test_createAdvancePaymentForm_allowed(self):
        """
        This test verifies that a user with the "Applicant" role has permission to access the "viewAdvancePaymentForm" view.
        Wait for an HTTP status code of 200 (OK).
        It also checks if the form instance in the context is of type TravelAdvanceSolicitationForm.
        """
        self.client.login(username='solicitante', password='password')
        response = self.client.get(reverse('viewAdvancePaymentForm'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['solicitation_form'], TravelAdvanceSolicitationForm)

    def test_createAdvancePaymentForm_not_allowed(self):
        """
        This test verifies that a user with the "Accountant" role does not have permission to access the "viewAdvancePaymentForm" view.
        Expect an HTTP status code of 302 (Redirect).
        """
        self.client.login(username='contable', password='password')
        response = self.client.get(reverse('viewAdvancePaymentForm'))
        self.assertEqual(response.status_code, 302) 