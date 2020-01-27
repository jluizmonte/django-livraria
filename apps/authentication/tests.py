from allauth.account.admin import EmailAddress
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AuthenticationTest(TestCase):

    def test_singup_get(self):
        response = self.client.post(reverse('account_signup'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')

    def test_signup_post(self):
        response = self.client.post(reverse('account_signup'), {'email': 'janedoe@gmail.com', 'password1': 'ArthurTuring'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('account_email_verification_sent'))

    def test_login_get(self):
        response = self.client.post(reverse('account_login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_login_post_client(self):
        password = make_password('ArthurTuring')
        user = User.objects.create(username='joedoe', password=password, email='joedoe@admin.com')
        EmailAddress.objects.create(user=user, verified=True, email=user.email)
        response = self.client.post(reverse('account_login'), {'login':user.email, 'password':'ArthurTuring'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('home'))