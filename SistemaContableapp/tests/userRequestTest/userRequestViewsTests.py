
from django.test import TestCase, Client
from django.urls import reverse


class ExteriorPaymentFormViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_form(self):
        url = reverse('viewExteriorPaymentForm')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exteriorPaymentForm.html')

    def test_post_form(self):
        url = reverse('viewExteriorPaymentForm')
        form_data = {
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
        response = self.client.post(url, form_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful form submission







