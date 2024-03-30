from unittest import TestCase

from SistemaContableApp.forms import ExteriorPaymentForm


class ExteriorPaymentFormTests(TestCase):
    
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
        form = ExteriorPaymentForm(data=form_data)
        self.assertTrue(form.is_valid())
        
        
    def test_form_invalid_data(self):
        """
        Test that the form does not validate with invalid data.
        """
        form_data = {
            'beneficiary_name': '',  # Campo requerido vacío
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
        form = ExteriorPaymentForm(data=form_data)
        self.assertFalse(form.is_valid())