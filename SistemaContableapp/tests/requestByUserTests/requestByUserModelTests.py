from django.test import TestCase
from SistemaContableApp.models import Charge_account, Requisition

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