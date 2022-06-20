from django.test import TestCase
# Create your tests here.
from django.http import response
from django.test import TestCase
from django.urls import reverse

class BaseTest(TestCase):
    def setUp(self):
        self.register_url=reverse('signup')
        self.user={
            'name': 'Omi',
            'email': 'om@gmail.com',
            'phone': '9757475959',
            'password': '123456789',
            'confirm_password': '123456789'
        }

        self.user_passwords_not_matching={
            'name': 'Omi',
            'email': 'om@gmail.com',
            'phone': '9757475959',
            'password': '123456789',
            'confirm_password': '123456789'
        }
        return super().setUp()

class RegisterTest(BaseTest):

    def test_can_view_page_correctly(self):
        response=self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'signup.html')

    def test_can_register_user(self):
        response = self.client.post(self.register_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302)

    def test_can_register_user_with_unmatching_password(self):
        response = self.client.post(self.register_url,self.user_passwords_not_matching,format='text/html')
        self.assertEqual(response.status_code,302)
