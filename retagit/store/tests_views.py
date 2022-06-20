from django.http import response
from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.register_url = reverse('signup')
        #self.flight = reverse('flight')
    def test_login_view(self):
        response = self.client.get(self.login_url)
        #print(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
    def test_register_view(self):
        response = self.client.get(self.register_url)
        #print(response)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
