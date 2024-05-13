from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from SistemaContableApp.views import *
from SistemaContableApp.models import *
from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Group
from SistemaContableApp.models import User, Group
from datetime import date, datetime
from SistemaContableApp.views import isLateRequest

class IsLateRequestTestCase(TestCase):
    def test_is_late_request_true(self):
        """
        Test case to verify that the isLateRequest function returns True
        when the request_date is after the 20th of the current month.
        """
        request_date = datetime(2024, 5, 21)
        self.assertTrue(isLateRequest(request_date))

    def test_is_late_request_false(self):
        """
        Test case to verify that the isLateRequest function returns False
        when the request_date is before the 20th of the current month.
        """
        request_date = datetime(2024, 5, 15)
        self.assertFalse(isLateRequest(request_date))

    def test_is_late_request_same_month(self):
        """
        Test case to verify that the isLateRequest function returns False
        when the request_date is on the 20th of the current month.
        """
        today = date.today()
        request_date = datetime(today.year, today.month, 20)
        self.assertFalse(isLateRequest(request_date))
        

def client():
    """
    Fixture function that returns a logged-in client for testing purposes.

    Returns:
        Client: A Django test client object.
    """
    username = 'testuser'
    email = 'testuser@example.com'
    name = 'Test User'
    user = User.objects.create_user(username=username, email=email, name=name, password='testpass')
    group = Group.objects.create(name='Solicitante')
    user.groups.add(group)
    user.save()

    c = Client()
    c.login(username=username, password='testpass')

    return c

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = client()
        
    def test_get_charge_account_form(self):
        """
        Test case to verify that the charge account form is rendered correctly
        on a GET request.
        """
        url = reverse('viewChargeAccountForm')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chargeAccountForm.html')

    def test_create_charge_account_form(self):
        """
        Test case to verify that a charge account is created correctly
        on a POST request with valid form data.
        """
        
        file_content = b'This is a test file.'
        uploaded_file = SimpleUploadedFile('test_file.txt', file_content)
        
        data = {
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
        response = self.client.post(reverse('viewChargeAccountForm'), data)
        self.assertEqual(response.status_code, 302)
        charge_account = Charge_account.objects.last()
        self.assertEqual(charge_account.name, 'Pablo')
        self.assertEqual(charge_account.identification, '1234567890')
        
        
        

    def test_get_exterior_payment_form(self):
        """
        Test case to verify that the exterior payment form is rendered correctly
        on a GET request.
        """
        url = reverse('viewExteriorPaymentForm')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'exteriorPaymentForm.html')
        
    def test_create_exterior_payment_form(self):
        """
        Test case to verify that an exterior payment is created correctly
        on a POST request with valid form data.
        """
        data = {
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
        response = self.client.post(reverse('viewExteriorPaymentForm'), data)
        self.assertEqual(response.status_code, 302)
        exterior_payment = Exterior_payment.objects.last()
        self.assertEqual(exterior_payment.beneficiary_name, 'Daniela')
        self.assertEqual(exterior_payment.beneficiary_document_no, '12345678')
        



    def test_get_requisition_form(self):
        """
        Test case to verify that the requisition form is rendered correctly
        on a GET request.
        """
        url = reverse('viewRequisitionForm')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'requisitionForm.html')
        
    def test_create_requisition_form(self):
        """
        Test case to verify that a requisition is created correctly
        on a POST request with valid form data.
        """
        data = {
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
        response = self.client.post(reverse('viewRequisitionForm'), data)
        self.assertEqual(response.status_code, 302)
        requisition = Requisition.objects.last()
        self.assertEqual(requisition.beneficiaryName, 'Pablo')
        self.assertEqual(requisition.idNumber, '1234567890')
        
        

    def test_get_legalization_form(self):
        """
        Test case to verify that the legalization form is rendered correctly
        on a GET request.
        """
        url = reverse('viewLegalizationForm')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'legalizationForm.html')
        
        
    def test_create_legalization_form(self):
        """
        Test case to verify that a legalization is created correctly
        on a POST request with valid form data.
        """
        legalization_data = {
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
        
        file_content = b'This is a test file.'
        uploaded_file = SimpleUploadedFile('test_file.txt', file_content)
        expense_data = {
            'expenses-TOTAL_FORMS': '1',
            'expenses-INITIAL_FORMS': '0',
            'expenses-MIN_NUM_FORMS': '0',
            'expenses-MAX_NUM_FORMS': '1000',
            'expenses-0-category': 'Transporte',
            'expenses-0-money_type': 'DOLARES',
            'expenses-0-money_value': 50000.00,
            'expenses-0-support' : uploaded_file,
            'expenses-0-support_no': '1',
            'expenses-0-third_person_name': 'pepe' ,
            'expenses-0-third_person_nit': '123',
            'expenses-0-concept': 'concepto0',

        }

        data = {**legalization_data, **expense_data}
        response = self.client.post(reverse('viewLegalizationForm'), data)
        self.assertEqual(response.status_code, 302)

        legalization = Legalization.objects.last()
        expenses = legalization.expenses.all()
        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0].category, 'Transporte')
        self.assertEqual(expenses[0].money_value, 50000.00)
        
        
        
    def test_get_advance_solicitation_form(self):
        """
        Test case to verify that the advance solicitation form is rendered correctly
        on a GET request.
        """
        url = reverse('viewAdvancePaymentForm')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'advancePaymentForm.html')
        
    def test_create_travel_advance_solicitation_form(self):
        """
        Test case to verify that a travel advance solicitation is created correctly
        on a POST request with valid form data.
        """
        advance_payment_data = {
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
        
        expense_data = {
            'expenses-TOTAL_FORMS': '2',
            'expenses-INITIAL_FORMS': '0',
            'expenses-MIN_NUM_FORMS': '0',
            'expenses-MAX_NUM_FORMS': '1000',
            'expenses-0-category': 'Transporte',
            'expenses-0-money_value': '50000.00',
            'expenses-1-category': 'Alojamiento',
            'expenses-1-money_value': '100000.00',
        }
        data = {**advance_payment_data, **expense_data}
        response = self.client.post(reverse('viewAdvancePaymentForm'), data)
        self.assertEqual(response.status_code, 302)

        advance_payment = AdvancePayment.objects.last()
        expenses = advance_payment.expenses.all()
        self.assertEqual(len(expenses), 2)
        self.assertEqual(expenses[0].category, 'Transporte')
        self.assertEqual(expenses[0].money_value, 50000.00)
        self.assertEqual(expenses[1].category, 'Alojamiento')
        self.assertEqual(expenses[1].money_value, 100000.00)
    
    
    


class ExcelGenerationTestCase(TestCase):
    def setUp(self):
        file_content = b'This is a test file.'
        uploaded_file = SimpleUploadedFile('test_file.txt', file_content)
        
        self.charge_account = Charge_account.objects.create(
            name= 'Pablo',
            identification= '1234567890',
            phone= '1234567890',
            city= 'Bogota',
            addres= 'Calle 123',
            date= '2023-04-01',
            value_letters= 'Cien mil pesos',
            value_numbers= '100000',
            concept= 'Concepto de prueba',
            bank= 'Banco de Prueba',
            type= 'De ahorros',
            account_number= '1234567890',
            cex= '12345',
            retentions= True,
            declarant= True,
            colombian_resident= True,
            supports= uploaded_file
        )
        

                
        self.exterior_payment = Exterior_payment.objects.create(
            beneficiary_name= 'Daniela',
            beneficiary_last_name= 'Londoño',
            beneficiary_document_type= 'DNI',
            beneficiary_document_no= '12345678',
            passport_number= 'ABC123456',
            passport_expedition_city= 'Cali',
            address= 'calle 25',
            bank_name= 'Bancolombia',
            account_type= 'Ahorros',
            swift_code= 'BOFAUS3N',
            iban_aba_code_type= 'IBAN',
            iban_aba_code= '01010101',
            account_name= 'Daniela Londoño',
            account_number= '1234567890',
            bank_address= 'calle 32'
        )
        
        self.requisition = Requisition.objects.create(
            date= '2023-04-01',
            beneficiaryName= 'Pablo',
            idNumber= '1234567890',
            charge= 'Developer',
            dependency= 'IT Department',
            cenco= '1234',
            value= '100000.50',
            concept= 'Reintegro colaboradores',
            description= 'Descripción de prueba',
            radicate= '12345',
            payment_order_code= '67890',
            paymentMethod= 'Nomina',
            typeAccount= 'De ahorros',
            account_number= '1234567890',
            authorName= 'Fernando'
        )
        
        self.travel_expenses_solicitation = Legalization.objects.create(
            legalization_date='2023-05-01',
            traveler_name='Nombre Viajero',
            identification='123456789',
            cost_center='1234',
            dependency='IT Department',
            destiny_city='Cali',
            travel_date='2023-05-10',
            return_date='2023-05-15',
            motive='Viaje de negocios',
            bank='Bancolombia',
            type_account='De ahorros',
            account_number='1234567890',
            orderer_name='Juan Pérez',
            elaborator_name='Ana López',
            descount_in_one_quote=True,
            advance_payment_value=500000.00,
            currency_type_of_advance_value='PESOS COLOMBIANOS'
        )

        self.advance_payment_solicitation = AdvancePayment.objects.create(
            radicate='12345',
            payment_order_code='67890',
            request_date='2023-05-01',
            traveler_name='Nombre Viajero',
            traveler_id='123456789',
            cost_center='1234',
            dependency='IT Department',
            destiny_city='Cali',
            travel_date='2023-05-10',
            return_date='2023-05-15',
            motive='Viaje de negocios',
            currency_type_of_advance_value='PESOS COLOMBIANOS',
            last_day_in_icesi='2023-05-09',
            descount_in_one_quote=True,
            orderer_name='Juan Pérez',
            elaborator_name='Ana López'
        )

    def test_generate_excel_charge_account(self):
        """
        Test case to verify that an Excel file is generated correctly
        for a charge account object.
        """
        filename = generateExcelChargeAccount(self.charge_account)
        self.assertTrue(filename.endswith('.xlsx'))

    def test_generate_excel_exterior_payment(self):
        """
        Test case to verify that an Excel file is generated correctly
        for an exterior payment object.
        """
        filename = generateExcelExteriorPayment(self.exterior_payment)
        self.assertTrue(filename.endswith('.xlsx'))

    def test_generate_excel_requisition(self):
        """
        Test case to verify that an Excel file is generated correctly
        for a requisition object.
        """
        filename = generateExcelRequisition(self.requisition)
        self.assertTrue(filename.endswith('.xlsx'))

    def test_generate_excel_legalization(self):
        """
        Test case to verify that an Excel file is generated correctly
        for a legalization object.
        """
        filename = generateExcelLegalization(self.travel_expenses_solicitation)
        self.assertTrue(filename.endswith('.xlsx'))

    def test_generate_excel_advance_payment(self):
        """
        Test case to verify that an Excel file is generated correctly
        for an advance payment object.
        """
        filename = generateExcelAdvancePayment(self.advance_payment_solicitation)
        self.assertTrue(filename.endswith('.xlsx'))