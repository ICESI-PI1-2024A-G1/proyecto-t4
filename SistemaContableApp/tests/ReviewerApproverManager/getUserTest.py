from django.test import TestCase, Client
from django.urls import reverse

class GetUsersTest(TestCase):
    """
    Test cases for the Get Users API endpoint.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        self.client = Client()

    def test_get_users_no_exclude_1(self):
        """
        Test retrieving users without excluding any roles.
        """
        response = self.client.get(reverse('get-users'), follow=True)

    def test_get_users_with_exclude_1(self):
        """
        Test retrieving users excluding certain roles.
        """
        response = self.client.get(reverse('get-users') + '?exclude={"admin": 1}', follow=True)

    def test_get_users_exception_1(self):
        """
        Test retrieving users with an invalid JSON exclude parameter.
        """
        response = self.client.get(reverse('get-users') + '?exclude=invalid_json', follow=True)

    def test_get_users_empty_request_1(self):
        """
        Test retrieving users with an empty request.
        """
        response = self.client.get(reverse('get-users'), follow=True)

    def test_get_users_invalid_exclude_1(self):
        """
        Test retrieving users with an invalid exclude parameter.
        """
        response = self.client.get(reverse('get-users') + '?exclude=invalid_param', follow=True)

    def test_get_users_invalid_method_1(self):
        """
        Test retrieving users with an invalid HTTP method.
        """
        response = self.client.post(reverse('get-users'), follow=True)

    def test_get_users_valid_request_1(self):
        """
        Test retrieving users with a valid exclude parameter.
        """
        response = self.client.get(reverse('get-users') + '?exclude={"viewer": 1}', follow=True)

    def test_get_users_no_exclude_2(self):
        """
        Test retrieving users without excluding any roles.
        """
        response = self.client.get(reverse('get-users'), follow=True)

    def test_get_users_with_exclude_2(self):
        """
        Test retrieving users excluding certain roles.
        """
        response = self.client.get(reverse('get-users') + '?exclude={"developer": 1}', follow=True)

    def test_get_users_exception_2(self):
        """
        Test retrieving users with an invalid JSON exclude parameter.
        """
        response = self.client.get(reverse('get-users') + '?exclude=invalid_json', follow=True)

    def test_get_users_empty_request_2(self):
        """
        Test retrieving users with an empty request.
        """
        response = self.client.get(reverse('get-users'), follow=True)

    def test_get_users_invalid_exclude_2(self):
        """
        Test retrieving users with an invalid exclude parameter.
        """
        response = self.client.get(reverse('get-users') + '?exclude=invalid_param', follow=True)

    def test_get_users_invalid_method_2(self):
        """
        Test retrieving users with an invalid HTTP method.
        """
        response = self.client.post(reverse('get-users'), follow=True)

    def test_get_users_valid_request_2(self):
        """
        Test retrieving users with a valid exclude parameter.
        """
        response = self.client.get(reverse('get-users') + '?exclude={"editor": 1}', follow=True)

    def test_get_users_no_exclude_3(self):
        """
        Test retrieving users without excluding any roles.
        """
        response = self.client.get(reverse('get-users'), follow=True)

    def test_get_users_with_exclude_3(self):
        """
        Test retrieving users excluding certain roles.
        """
        response = self.client.get(reverse('get-users') + '?exclude={"customer": 1}', follow=True)

    def test_get_users_exception_3(self):
        """
        Test retrieving users with an invalid JSON exclude parameter.
        """
        response = self.client.get(reverse('get-users') + '?exclude=invalid_json', follow=True)

    def test_get_users_empty_request_3(self):
        """
        Test retrieving users with an empty request.
        """
        response = self.client.get(reverse('get-users'), follow=True)

    def test_get_users_invalid_exclude_3(self):
        """
        Test retrieving users with an invalid exclude parameter.
        """
        response = self.client.get(reverse('get-users') + '?exclude=invalid_param', follow=True)

    def test_get_users_invalid_method_3(self):
        """
        Test retrieving users with an invalid HTTP method.
        """
        response = self.client.post(reverse('get-users'), follow=True)

    def test_get_users_valid_request_3(self):
        """
        Test retrieving users with a valid exclude parameter.
        """
        response = self.client.get(reverse('get-users') + '?exclude={"manager": 1}', follow=True)




