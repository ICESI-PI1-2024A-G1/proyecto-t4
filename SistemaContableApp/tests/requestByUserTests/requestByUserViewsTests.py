from django.test import TestCase, Client
from django.urls import reverse
from SistemaContableApp.models import *
from SistemaContableApp.forms import *
from django.core.files.uploadedfile import SimpleUploadedFile


class ChargeAccountFormViewTests(TestCase):
    def setUp(self):
        
        file_content = b'This is a test file.'
        uploaded_file = SimpleUploadedFile('test_file.txt', file_content)
        
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
            'colombian_resident': True,
            'supports': uploaded_file
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




class CreateLegalizationFormViewTests(TestCase):
    def setUp(self):
        file_content = b'This is a test file.'
        uploaded_file = SimpleUploadedFile('test_file.txt', file_content)
        
        self.client = Client()
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
        self.expense_data = {
            'category': 'Transporte',
            'support': uploaded_file,
            'support_no': '12345',
            'third_person_name': 'Transportes S.A.',
            'third_person_nit': '123456789',
            'concept': 'Taxis y buses',
            'money_type': 'PESOS COLOMBIANOS',
            'money_value': 100000.00
        }

    def test_get_form(self):
        url = reverse('viewLegalizationForm')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'legalizationForm.html')

    def test_post_form(self):
        url = reverse('viewLegalizationForm')
        solicitation_form_data = self.legalization_data.copy()
        expense_formset_data = {
            'expenses-TOTAL_FORMS': '1',
            'expenses-INITIAL_FORMS': '0',
            'expenses-MIN_NUM_FORMS': '0',
            'expenses-MAX_NUM_FORMS': '1000',
            'expenses-0-category': self.expense_data['category'],
            'expenses-0-support' : self.expense_data['support'],
            'expenses-0-support_no': self.expense_data['support_no'],
            'expenses-0-third_person_name': self.expense_data['third_person_name'],
            'expenses-0-third_person_nit': self.expense_data['third_person_nit'],
            'expenses-0-concept': self.expense_data['concept'],
            'expenses-0-money_type': self.expense_data['money_type'],
            'expenses-0-money_value': self.expense_data['money_value']
        }
        form_data = {**solicitation_form_data, **expense_formset_data}
        response = self.client.post(url, form_data)
        self.assertEqual(response.status_code, 302)
        legalization = Legalization.objects.first()
        self.assertIsNotNone(legalization)
        self.assertEqual(legalization.traveler_name, 'Juan Pérez')
        expense = LegalizationExpense.objects.first()
        self.assertIsNotNone(expense)
        self.assertEqual(expense.category, 'Transporte')
        
        
        
        


class CreateAdvancePaymentFormViewTests(TestCase):
    def setUp(self):
        self.client = Client()
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
        self.expense_data = {
            'category': 'Transporte',
            'money_value': 100000.00
        }

    def test_get_form(self):
        url = reverse('viewAdvancePaymentForm')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'advancePaymentForm.html')

    def test_post_form(self):
        url = reverse('viewAdvancePaymentForm')
        solicitation_form_data = self.advance_payment_data.copy()
        expense_formset_data = {
            'expenses-TOTAL_FORMS': '1',
            'expenses-INITIAL_FORMS': '0',
            'expenses-MIN_NUM_FORMS': '0',
            'expenses-MAX_NUM_FORMS': '1000',
            'expenses-0-category': self.expense_data['category'],
            'expenses-0-money_value': self.expense_data['money_value']
        }
        form_data = {**solicitation_form_data, **expense_formset_data}
        response = self.client.post(url, form_data)
        self.assertEqual(response.status_code, 302)
        advance_payment = AdvancePayment.objects.first()
        self.assertIsNotNone(advance_payment)
        self.assertEqual(advance_payment.traveler_name, 'Juan Pérez')
        expense = AdvanceExpense.objects.first()
        self.assertIsNotNone(expense)
        self.assertEqual(expense.category, 'Transporte')