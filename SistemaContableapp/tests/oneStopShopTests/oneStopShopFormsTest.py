from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from SistemaContableApp.forms import OneStopShopForm, AttachedDocumentForm
from SistemaContableApp.models import State

class FormTestCase(TestCase):

    def setUp(self):

        self.state = State.objects.create(state = "Pendiente de aceptación", color = "gray")


    def testOneStopShopValidForm(self):

        formData =  {
            'creationDate': '2023-04-01',
            'creator': 'John Doe',
            'type': 'Solicitud',
            'supplier': 'Acme Inc.',
            'supplierId': '12345',
            'documentNumber': 'DOC001',
            'concept': 'Trasport',
            'supplierEmail':'user@corre.com',
            'moneyType': 'USD',
            'amount': 1000,
            'cenco': 'CENCO1',
            'cexNumber': 'CEX001',
            'observations': 'Ninguna',
            'currentState': self.state.pk,
            'closeDate': '2023-04-30',
        }
        form = OneStopShopForm(data=formData)
        self.assertTrue(form.is_valid())

    def testAttachedDocumentValidForm(self):
        
        formData = {'file': SimpleUploadedFile('media/testFile.pdf',b'file_content')}
        form = AttachedDocumentForm(files=formData)
        self.assertTrue(form.is_valid())

    def testOneStopShopInvalidForm(self):
        formData =  {
            'creationDate': '2023-04-01',
            'creator': 'John Doe',
            'type': 'Solicitud',
            'supplier': 'Acme Inc.',
            'supplierId': '12345',
            'documentNumber': 'DOC001',
            'supplierEmail':'user@corre.com',
            'moneyType': 'USD',
            'amount': 1000,
            'cenco': 'CENCO1',
            'cexNumber': 'CEX001',
            'observations': 'Ninguna',
            'currentState': self.state.pk,
            'closeDate': '2023-04-30',
        }
        form = OneStopShopForm(data=formData)
        self.assertFalse(form.is_valid())

    def testAttachedDocumentInvalidForm(self):
        
        formData = {'file': 'testFile.pdf'}
        form = AttachedDocumentForm(files=formData)
        self.assertFalse(form.is_valid())