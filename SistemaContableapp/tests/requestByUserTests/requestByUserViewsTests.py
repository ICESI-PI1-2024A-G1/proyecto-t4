from django.test import TestCase, Client
from django.urls import reverse

class ChargeAccountFormViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.form_data = {
            'name': 'Pablo',
            'identification': '1234567890',
            'phone': '1234567890',
            'city': 'Bogota',
            'addres': 'Calle 123',
            'date': '2023-04-01',
            'value_letters': 'Cien mil pesos',
            'value_numbers': '100000',
            'concept': 'Concepto de prueba',
            'bank': 'Banco de Prueba',
            'type': 'De ahorros',
            'account_number': '1234567890',
            'cex': '12345',
            'retentions': True,
            'declarant': True,
            'colombian_resident': True
        }

    def test_get_form(self):
        """
        Test that the form is rendered correctly on a GET request.
        """
        url = reverse('viewChargeAccountForm')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chargeAccountForm.html')

    def test_post_form(self):
        """
        Test that the form is processed correctly on a POST request with valid data.
        """
        url = reverse('viewChargeAccountForm')
        response = self.client.post(url, self.form_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission

class RequisitionFormViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.form_data = {
            'date': '2023-04-01',
            'beneficiaryName': 'Pablo',
            'idNumber': '1234567890',
            'charge': 'Developer',
            'dependency': 'IT Department',
            'cenco': '1234',
            'value': '100000.50',
            'concept': 'Reintegro colaboradores',
            'description': 'Descripción de prueba',
            'radicate': '12345',
            'payment_order_code': '67890',
            'paymentMethod': 'Nomina',
            'typeAccount': 'De ahorros',
            'account_number': '1234567890',
            'authorName': 'Fernando'
        }

    def test_get_form(self):
        """
        Test that the form is rendered correctly on a GET request.
        """
        url = reverse('viewRequisitionForm')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'requisitionForm.html')

    def test_post_form(self):
        """
        Test that the form is processed correctly on a POST request with valid data.
        """
        url = reverse('viewRequisitionForm')
        response = self.client.post(url, self.form_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission
        
        
class ExteriorPaymentFormViewTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.form_data = {
            'beneficiary_name': 'Daniela',
            'beneficiary_last_name': 'Londoño',
            'beneficiary_document_type': 'DNI',
            'beneficiary_document_no': '12345678',
            'passport_number': 'ABC123456',
            'passport_expedition_city': 'Cali',
            'address': 'calle 25',
            'bank_name': 'Bancolombia',
            'account_type': 'Ahorros',
            'swift_code': 'BOFAUS3N',
            'iban_aba_code_type': 'IBAN',
            'iban_aba_code': '01010101',
            'account_name': 'Daniela Londoño',
            'account_number': '1234567890',
            'bank_address': 'calle 32'
        }

    def test_get_form(self):
        url = reverse('viewExteriorPaymentForm')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exteriorPaymentForm.html')

    def test_post_form(self):
        url = reverse('viewExteriorPaymentForm')
        response = self.client.post(url, self.form_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission






