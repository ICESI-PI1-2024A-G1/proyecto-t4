from django.test import TestCase
from SistemaContableApp.models import *

class ChargeAccountModelTests(TestCase):
    def setUp(self):
        self.charge_account_data = {
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

    def test_create_charge_account(self):
        """
        Test creating a new Charge_account instance with valid data.
        """
        charge_account = Charge_account.objects.create(**self.charge_account_data)
        self.assertIsInstance(charge_account, Charge_account)


class RequisitionModelTests(TestCase):
    def setUp(self):
        self.requisition_data = {
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

    def test_create_requisition(self):
        """
        Test creating a new Requisition instance with valid data.
        """
        requisition = Requisition.objects.create(**self.requisition_data)
        self.assertIsInstance(requisition, Requisition)
        
        
class ExteriorPaymentModelTests(TestCase):
    
    def setUp(self):
        self.exteriorPayment_data = {
            'beneficiary_name': 'Daniela',
            'beneficiary_last_name':'Londoño',
            'beneficiary_document_type':'DNI',
            'beneficiary_document_no':'12345678',
            'passport_number':'ABC123456',
            'passport_expedition_city':'Cali',
            'address':'calle 25',
            'bank_name':'Bancolombia',
            'account_type':'Ahorros',
            'swift_code':'BOFAUS3N',
            'iban_aba_code_type':'IBAN',
            'iban_aba_code':'01010101',
            'account_name':'Daniela Londoño',
            'account_number':'1234567890',
            'bank_address':'calle 32'
        }
        
        self.expected_fields = {
            'id',
            'beneficiary_name',
            'beneficiary_last_name',
            'beneficiary_document_type',
            'beneficiary_document_no',
            'passport_number',
            'passport_expedition_city',
            'address',
            'bank_name',
            'account_type',
            'swift_code',
            'iban_aba_code_type',
            'iban_aba_code',
            'account_name',
            'account_number',
            'bank_address'
        }
    
    def test_create_exterior_payment(self):
        """
        Test that we can create an exterior payment instance with valid data.
        """
        exterior_payment = Exterior_payment.objects.create(**self.exteriorPayment_data)
        self.assertIsInstance(exterior_payment, Exterior_payment)


    def test_exterior_payment_fields(self):
        """
        Test that the exterior payment model has all the expected fields.
        """
        exterior_payment = Exterior_payment()
        fields = [field.name for field in exterior_payment._meta.get_fields()]

        self.assertCountEqual(fields, self.expected_fields)


    def test_exterior_payment_choices(self):
        """
        Test that the exterior payment model has the correct choices for account_type and iban_aba_code_type fields.
        """
        account_type_choices = [choice for choice in Exterior_payment.BANK_ACCOUNT_TYPE]
        expected_account_type_choices = [('Ahorros', 'Ahorros'), ('Corriente', 'Corriente')]
        self.assertCountEqual(account_type_choices, expected_account_type_choices)

        iban_aba_code_type_choices = [choice for choice in Exterior_payment.IBAN_ABA_CODE_TYPE]
        expected_iban_aba_code_type_choices = [('IBAN', 'IBAN'), ('ABA', 'ABA')]
        self.assertCountEqual(iban_aba_code_type_choices, expected_iban_aba_code_type_choices)
        
        
        
class LegalizationModelTests(TestCase):
    def setUp(self):
        self.legalization_data = {
            'legalization_date': '2023-05-01',
            'traveler_name': 'Juan Pérez',
            'identification': '1234567890',
            'cost_center': '1234',
            'dependency': 'Departamento de Ventas',
            'destiny_city': 'Bogotá',
            'travel_date': '2023-04-15',
            'return_date': '2023-04-20',
            'motive': 'Reunión de negocios',
            'bank': 'Banco de Bogotá',
            'type_account': 'De ahorros',
            'account_number': '1234567890',
            'orderer_name': 'María Rodríguez',
            'elaborator_name': 'Pedro Gómez',
            'descount_in_one_quote': True,
            'advance_payment_value': 1000000.00,
            'currency_type_of_advance_value': 'PESOS COLOMBIANOS'
        }
        
        
    def test_create_legalization(self):
        """
        Test creating a new Legalization instance with valid data.
        """
        legalization = Legalization.objects.create(**self.legalization_data)
        self.assertIsInstance(legalization, Legalization)


    def test_fields_legalization(self):
        """
        Test that the legalization model has the expected field value.
        """ 
        legalization = Legalization.objects.create(**self.legalization_data)
        self.assertIsInstance(legalization, Legalization)
        self.assertEqual(legalization.traveler_name, 'Juan Pérez')
        self.assertEqual(legalization.currency_type_of_advance_value, 'PESOS COLOMBIANOS')

        
        

class AdvancePaymentModelTests(TestCase):
    def setUp(self):
        self.advance_payment_data = {
            'radicate': '12345',
            'payment_order_code': '67890',
            'request_date': '2023-05-01',
            'traveler_name': 'Juan Pérez',
            'traveler_id': '1234567890',
            'cost_center': '1234',
            'dependency': 'Departamento de Ventas',
            'destiny_city': 'Bogotá',
            'travel_date': '2023-05-15',
            'return_date': '2023-05-20',
            'motive': 'Reunión de negocios',
            'currency_type_of_advance_value': 'PESOS COLOMBIANOS',
            'last_day_in_icesi': '2023-05-14',
            'descount_in_one_quote': True,
            'orderer_name': 'María Rodríguez',
            'elaborator_name': 'Pedro Gómez'
        }


    def test_create_advance_payment(self):
        """
        Test creating a new AdvancePayment instance with valid data.
        """
        advance = AdvancePayment.objects.create(**self.advance_payment_data)
        self.assertIsInstance(advance, AdvancePayment)
        
        
        
    def test_fields_advance_payment(self):
        """
        Test that the advance payment model has the expected field value.
        """
        advance_payment = AdvancePayment.objects.create(**self.advance_payment_data)
        self.assertIsInstance(advance_payment, AdvancePayment)
        self.assertEqual(advance_payment.traveler_name, 'Juan Pérez')
        self.assertEqual(advance_payment.currency_type_of_advance_value, 'PESOS COLOMBIANOS')
