from django.test import TestCase
from django.test import Client


class AuthenticationTest(TestCase):
    client = Client()

    def test_signup(self):
        response = self.client.post('/autenticacao/cadastro/', {'email': 'janedoe@gmail.com', 'password1': 'ArthurTuring'})
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(response, 'account/messages/email_confirmation_sent.txt')
