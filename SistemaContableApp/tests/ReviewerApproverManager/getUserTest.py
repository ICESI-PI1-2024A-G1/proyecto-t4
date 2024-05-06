from django.test import TestCase, Client
from django.urls import reverse

class GetUsersTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_users_no_exclude(self):
        response = self.client.get(reverse('get-users'), follow=True)

    def test_get_users_with_exclude(self):
        response = self.client.get(reverse('get-users') + '?exclude={"gestor": 1}', follow=True)

    def test_get_users_exception(self):
        response = self.client.get(reverse('get-users') + '?exclude=invalid_json', follow=True)

    def test_get_users_empty_request(self):
        response = self.client.get(reverse('get-users'), follow=True)

    def test_get_users_invalid_exclude(self):
        response = self.client.get(reverse('get-users') + '?exclude=invalid_param', follow=True)

    def test_get_users_invalid_method(self):
        response = self.client.post(reverse('get-users'), follow=True)

    def test_get_users_valid_request(self):
        response = self.client.get(reverse('get-users') + '?exclude={"gestor": 1}', follow=True)


