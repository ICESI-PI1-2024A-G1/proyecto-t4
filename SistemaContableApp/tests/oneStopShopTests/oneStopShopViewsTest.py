from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from SistemaContableApp.models import Following, AttachedDocument, State

class ViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.state = State.objects.create(state="Pendiente de aceptación", color="gray")

    def testSummaryOneStopShopView(self):
        """
        Test the summaryOneStopShop view.

        It verifies that the view returns a status code 200, uses the correct template, and passes required context data.

        Expected behavior:
            - The view should return a status code 200.
            - The view should use the template 'summaryOneStopShop.html'.
            - The view should pass 'followingData' in the context.
        """
        response = self.client.get(reverse('summaryOneStopShop'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'summaryOneStopShop.html')
        self.assertTrue('followingData' in response.context)

    def testFullOneStopShopView(self):
        """
        Test the fullOneStopShop view.

        It verifies that the view returns a status code 200, uses the correct template, and passes required context data.

        Expected behavior:
            - The view should return a status code 200.
            - The view should use the template 'fullOneStopShop.html'.
            - The view should pass 'followingData' and 'files' in the context.
        """
        response = self.client.get(reverse('fullOneStopShop'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fullOneStopShop.html')
        self.assertTrue('followingData' in response.context)
        self.assertTrue('files' in response.context)

    def testOneStopShopFormViewGet(self):
        """
        Test the OneStopShopForm view with a GET request.

        It verifies that the view returns a status code 200, uses the correct template, and passes required context data.

        Expected behavior:
            - The view should return a status code 200.
            - The view should use the template 'oneStopShopForm.html'.
            - The view should pass 'oneStopShopForm' and 'attachedDocumentForm' in the context.
        """
        response = self.client.get(reverse('OneStopShopForm'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'oneStopShopForm.html')
        self.assertTrue('oneStopShopForm' in response.context)
        self.assertTrue('attachedDocumentForm' in response.context)

    def testOneStopShopFormViewPostValid(self):
        """
        Test the OneStopShopForm view with a POST request containing valid data.

        It verifies that the view redirects after successful form submission and creates the expected Following and AttachedDocument instances.

        Expected behavior:
            - The view should redirect to 'OneStopShopForm' after form submission.
            - A Following instance with the provided creator should be created.
            - An AttachedDocument instance associated with the created Following should be created.
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

        fileData = {'file': SimpleUploadedFile('media/testFile.pdf', b'file_content')}

        data = {**formData, **fileData}

        response = self.client.post(reverse('OneStopShopForm'), data)
        following = Following.objects.get(creator=formData['creator'])
        self.assertRedirects(response, reverse('OneStopShopForm'))
        self.assertTrue(Following.objects.filter(creator=formData['creator']).exists())
        self.assertTrue(AttachedDocument.objects.filter(associatedFollowing=following).exists())
