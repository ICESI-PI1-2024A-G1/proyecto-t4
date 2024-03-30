
from django.test import TestCase
from SistemaContableApp.models import Following, AttachedDocument, State

class ModelTestCase(TestCase):
    def test_Following_model(self):
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

    def test_AttachedDocument_model(self):
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
        attached_document = AttachedDocument.objects.create(
            file='test_file.pdf',
            associatedFollowing=following
        )
        self.assertEqual(str(attached_document), 'test_file.pdf')
        self.assertEqual(attached_document.associatedFollowing,following)

