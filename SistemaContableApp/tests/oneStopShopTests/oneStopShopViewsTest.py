from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from SistemaContableApp.models import Following, AttachedDocument, State, Rol
from django.contrib.auth import get_user_model
from django.test import RequestFactory

class ViewTestCase(TestCase):

    def setUp(self):
        """
        Set up the necessary objects and data for the test case.

        This method is called before each individual test method is run.
        It creates a user with the role 'Administrador' and sets up a RequestFactory object.

        Args:
            self: The current instance of the test case.

        Returns:
            None
        """
        User = get_user_model()

        self.rol_ventanilla_unica = Rol.objects.create(rol='Ventanilla única')

        self.rol_Administrador = Rol.objects.create(rol='Administrador')       
        self.admin_user = User.objects.create_user(
            username='Admin',
            email='admin@gmail.com',
            name='Administrador',
            password='password'
        )
        self.admin_user.rol = self.rol_Administrador
        self.admin_user.save()

        self.ventanilla_unica_user = User.objects.create_user(
            username='Ventanilla',
            email='ventanilla@gmail.com',
            name='Ventanilla única',
            password='password'
        )
        self.ventanilla_unica_user.rol = self.rol_ventanilla_unica
        self.ventanilla_unica_user.save()

        self.factory = RequestFactory()
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
        self.client.login(username='Admin', password='password')
        
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
        self.client.login(username='Admin', password='password')


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
        self.client.force_login(self.ventanilla_unica_user)

        response = self.client.get(reverse('OneStopShopForm'), follow=True)
        self.assertEqual(response.status_code, 200)
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
        self.client.force_login(self.ventanilla_unica_user)

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

        response = self.client.post(reverse('OneStopShopForm'), data, follow=True)
        following_exists = Following.objects.filter(creator=formData['creator']).exists()
        self.assertTrue(following_exists)

        if following_exists:
            following = Following.objects.get(creator=formData['creator'])
            self.assertTrue(AttachedDocument.objects.filter(associatedFollowing=following).exists())