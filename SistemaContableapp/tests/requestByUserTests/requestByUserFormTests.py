from django.test import TestCase
from SistemaContableApp.forms import ChargeAccountForm, RequisitionForm

class ChargeAccountFormTests(TestCase):
    def setUp(self):
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
        self.form_data_empty = {
            'name': '',
            'identification': '',
            'phone': '',
            'city': '',
            'addres': '',
            'date': '',
            'value_letters': '',
            'value_numbers': '',
            'concept': '',
            'bank': '',
            'type': '',
            'account_number': '',
            'cex': '',
            'retentions': False,
            'declarant': False,
            'colombian_resident': False
        }

    def test_valid_form(self):
        """ Test that the form is valid with valid input data. """
        form = ChargeAccountForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_blank_fields(self):
        """ Test that the form is invalid if required fields are left blank. """
        form = ChargeAccountForm(data=self.form_data_empty)
        self.assertFalse(form.is_valid())

class RequisitionFormTests(TestCase):
    def setUp(self):
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
        self.form_data_empty = {
            'date': '',
            'beneficiaryName': '',
            'idNumber': '',
            'charge': '',
            'dependency': '',
            'cenco': '',
            'value': '',
            'concept': '',
            'description': '',
            'radicate': '',
            'payment_order_code': '',
            'paymentMethod': '',
            'typeAccount': '',
            'account_number': '',
            'authorName': ''
        }

    def test_valid_form(self):
        """ Test that the form is valid with valid input data. """
        form = RequisitionForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_blank_fields(self):
        """ Test that the form is invalid if required fields are left blank. """
        form = RequisitionForm(data=self.form_data_empty)
        self.assertFalse(form.is_valid())