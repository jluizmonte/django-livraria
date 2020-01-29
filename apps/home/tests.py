from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class HomeTest(TestCase):

    def test_home_without_login(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('main'))

    def test_home_as_user(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=False)
        self.client.force_login(user)
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('main'))

    def test_home_as_superuser(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('administrative'))