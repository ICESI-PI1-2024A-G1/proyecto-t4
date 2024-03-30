from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from SistemaContableApp.models import Following, AttachedDocument,State

class ViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.state = State.objects.create(state = "Pendiente de aceptación", color = "gray")
    
    def testSummaryOneStopShopView(self):
        response = self.client.get(reverse('summaryOneStopShop'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'summaryOneStopShop.html')
        self.assertTrue('followingData' in response.context)
        
    def testFullOneStopShopView(self):
        response = self.client.get(reverse('fullOneStopShop'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'fullOneStopShop.html')
        self.assertTrue('followingData' in response.context)
        self.assertTrue('files' in response.context)

    def testOneStopShopConfirmationView(self):
        response = self.client.get(reverse('confirmation'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'oneStopShopConfirmation.html')

    def testOneStopShopFormViewGet(self):
        response = self.client.get(reverse('OneStopShopForm'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'oneStopShopForm.html')
        self.assertTrue('oneStopShopForm' in response.context)
        self.assertTrue('attachedDocumentForm' in response.context)

    def testOneStopShopFormViewPostValid(self):
        data = {
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
        form_data = {
            'creationDate': data['creationDate'],
            'creator': data['creator'],
            'type': data['type'],
            'supplier': data['supplier'],
            'supplierId': data['supplierId'],
            'documentNumber': data['documentNumber'],
            'concept': data['concept'],
            'supplierEmail':data['supplierEmail'],
            'moneyType': data['moneyType'],
            'amount': data['amount'],
            'cenco': data['cenco'],
            'cexNumber': data['cexNumber'],
            'observations': data['observations'],
            'currentState': data['currentState'],
            'closeDate': data['closeDate'],
        }

        file_data = {'file': SimpleUploadedFile('media/testFile.pdf',b'file_content')}

        data = {**form_data, **file_data}

        response = self.client.post(reverse('OneStopShopForm'), data) 
        following = Following.objects.get(creator = form_data['creator'])   
        self.assertRedirects(response,reverse('confirmation'))
        self.assertTrue(Following.objects.filter(creator = form_data['creator']).exists())
        self.assertTrue(AttachedDocument.objects.filter(associatedFollowing = following).exists())