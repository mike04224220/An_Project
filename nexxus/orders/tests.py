from django.test import TestCase
from django.urls import reverse # Go back
from django.contrib.auth import get_user_model # Account is logged

class MyOrderViewTest(TestCase):

    def test_no_logged_user_should_redirect(self):
        url = reverse('my_order')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302) # Is redirecting ?
        self.assertEqual(response.url, '/usuarios/login/?next=/pedidos/mi-orden')

    def test_logged_user_should_redirect(self):
        url = reverse('my_order')
        user = get_user_model().objects.create(username="test")
        self.client.force_login(user) # What loggin
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)