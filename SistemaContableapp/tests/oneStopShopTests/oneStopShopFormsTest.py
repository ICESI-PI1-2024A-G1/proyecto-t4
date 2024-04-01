from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from SistemaContableApp.forms import OneStopShopForm, AttachedDocumentForm
from SistemaContableApp.models import State

class FormTestCase(TestCase):

    def setUp(self):
        self.state = State.objects.create(state="Pendiente de aceptación", color="gray")

    def testOneStopShopValidForm(self):
        """
        Test the OneStopShopForm with valid data.

        It verifies that the OneStopShopForm is valid when provided with valid data.

        Test data:
            - Valid form data.

        Expected behavior:
            - The form should be valid.
        """
        formData = {
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
        """
        Test the AttachedDocumentForm with valid data.

        It verifies that the AttachedDocumentForm is valid when provided with valid data.

        Test data:
            - Valid file data.

        Expected behavior:
            - The form should be valid.
        """
        formData = {'file': SimpleUploadedFile('media/testFile.pdf', b'file_content')}
        form = AttachedDocumentForm(files=formData)
        self.assertTrue(form.is_valid())

    def testOneStopShopInvalidForm(self):
        """
        Test the OneStopShopForm with invalid data.

        It verifies that the OneStopShopForm is invalid when provided with incomplete data.

        Test data:
            - Incomplete form data.

        Expected behavior:
            - The form should be invalid.
        """
        formData = {
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
            # 'closeDate' field is missing
        }
        form = OneStopShopForm(data=formData)
        self.assertFalse(form.is_valid())

    def testAttachedDocumentInvalidForm(self):
        """
        Test the AttachedDocumentForm with invalid data.

        It verifies that the AttachedDocumentForm is invalid when provided with incorrect file data.

        Test data:
            - Invalid file data.

        Expected behavior:
            - The form should be invalid.
        """
        formData = {'file': 'testFile.pdf'}  # Incorrect file data
        form = AttachedDocumentForm(files=formData)
        self.assertFalse(form.is_valid())
