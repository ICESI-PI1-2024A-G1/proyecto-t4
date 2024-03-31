from django.test import TestCase
from SistemaContableApp.forms import *

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
        
        
        
        
class ExteriorPaymentFormTests(TestCase):
    
    def setUp(self):
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
        
        self.form_data_invalid = {
            'beneficiary_name': '', 
            'beneficiary_last_name': '',
            'beneficiary_document_type': '',
            'beneficiary_document_no': '',  
            'passport_number': '',
            'passport_expedition_city': '',
            'address': 'calle 25',
            'bank_name': 'Bancolombia',
            'account_type': 'Ahorros',
            'swift_code': '111111111111', 
            'iban_aba_code_type': 'IBAN',
            'iban_aba_code': '',
            'account_name': 'Daniela Londoño',
            'account_number': '1234567890',
            'bank_address': 'calle 32'
        }
    
    def test_form_fields(self):
        """
        Test that the form contains all the expected fields.
        """
        form = ExteriorPaymentForm()
        expected_fields = [
            'beneficiary_name', 'beneficiary_last_name', 'beneficiary_document_type',
            'beneficiary_document_no', 'passport_number', 'passport_expedition_city',
            'address', 'bank_name', 'account_type', 'swift_code', 'iban_aba_code_type',
            'iban_aba_code', 'account_name', 'account_number', 'bank_address'
        ]
        self.assertEqual(list(form.fields.keys()), expected_fields)
    
    
    def test_form_valid_data(self):
        """
        Test that the form validates with valid data.
        """
        form = ExteriorPaymentForm(data=self.form_data)
        self.assertTrue(form.is_valid())
        
        
    def test_form_invalid_data(self):
        """
        Test that the form does not validate with invalid data.
        """      
        form = ExteriorPaymentForm(data=self.form_data_invalid)
        self.assertFalse(form.is_valid())