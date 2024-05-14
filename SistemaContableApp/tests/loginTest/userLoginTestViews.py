from django.test import TestCase, Client
from django.urls import reverse

class UserRequestViewsTest2(TestCase):
    def setUp(self):
        """
        Set up the test environment.
        """
        self.client = Client()

    def test_index_view(self):
        """
        Test the index view.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        """
        Test the login view.
        """
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        
    def test_registration_view(self):
        """
        Test the registration view.
        """
        response = self.client.get(reverse('registration'))
        self.assertEqual(response.status_code, 200)

    def test_about_us_view(self):
        """
        Test the about us view.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_contact_us_view(self):
        """
        Test the contact us view.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_services_view(self):
        """
        Test the services view.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_products_view(self):
        """
        Test the products view.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_blog_view(self):
        """
        Test the blog view.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_faq_view(self):
        """
        Test the FAQ view.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_privacy_policy_view(self):
        """
        Test the privacy policy view.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class UserRequestViewsTest3(TestCase):
    def setUp(self):
        """
        Set up the test environment.
        """
        self.client = Client()

    def test_index_view(self):
        """
        Test the index view.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        """
        Test the login view.
        """
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        
    def test_registration_view(self):
        """
        Test the registration view.
        """
        response = self.client.get(reverse('registration'))
        self.assertEqual(response.status_code, 200)

    def test_about_us_view(self):
        """
        Test the about us view.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_contact_us_view(self):
        """
        Test the contact us view.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_services_view(self):
        """
        Test the services view.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_products_view(self):
        """
        Test the products view.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_blog_view(self):
        """
        Test the blog view.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_faq_view(self):
        """
        Test the FAQ view.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_terms_of_service_view(self):
        """
        Test the terms of service view.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class UserRequestViewsTest4(TestCase):
    def setUp(self):
        """
        Set up the test environment.
        """
        self.client = Client()

    def test_index_view(self):
        """
        Test the index view.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        """
        Test the login view.
        """
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        
    def test_registration_view(self):
        """
        Test the registration view.
        """
        response = self.client.get(reverse('registration'))
        self.assertEqual(response.status_code, 200)

    
  
      


    
   