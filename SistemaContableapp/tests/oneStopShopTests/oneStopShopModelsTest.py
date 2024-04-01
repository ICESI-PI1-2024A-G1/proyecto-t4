
from django.test import TestCase
from SistemaContableApp.models import Following, AttachedDocument, State

class ModelTestCase(TestCase):

    def testFollowingModel(self):
        """
        Test the Following model.

        It verifies that the Following model creates instances correctly and returns the expected string representation.

        Expected behavior:
            - The string representation of a Following instance should be '<type> - <cenco>'.
        """
        state = State.objects.create(state="Pendiente de aceptación", color="gray")
        following = Following.objects.create(
            creationDate='2023-04-01',
            creator='John Doe',
            type='Solicitud',
            supplier='Acme Inc.',
            supplierId='12345',
            documentNumber='DOC001',
            manager='Jane Smith',
            concept='Compra de suministros',
            moneyType='USD',
            amount=1000,
            cenco='CENCO1',
            cexNumber='CEX001',
            observations='Ninguna',
            currentState=state,
            closeDate='2023-04-30',
        )
        self.assertEqual(str(following), 'Solicitud - CENCO1')

    def testAttachedDocumentModel(self):
        """
        Test the AttachedDocument model.

        It verifies that the AttachedDocument model creates instances correctly and returns the expected string representation.

        Expected behavior:
            - The string representation of an AttachedDocument instance should be the name of the file.
            - The associatedFollowing field should be associated with a Following instance.
        """
        following = Following.objects.create(
            creationDate='2023-04-01',
            creator='John Doe',
            type='Solicitud',
            supplier='Acme Inc.',
            supplierId='12345',
            documentNumber='DOC001',
            manager='Jane Smith',
            concept='Compra de suministros',
            moneyType='USD',
            amount=1000,
            cenco='CENCO1',
            cexNumber='CEX001',
            observations='Ninguna',
            currentState=State.objects.create(state="Pendiente de aceptación", color="gray"),
            closeDate='2023-04-30',
        )
        attachedDocument = AttachedDocument.objects.create(
            file='test_file.pdf',
            associatedFollowing=following
        )
        self.assertEqual(str(attachedDocument), 'test_file.pdf')
        self.assertEqual(attachedDocument.associatedFollowing, following)


