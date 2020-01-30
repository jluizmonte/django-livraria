from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class UserTest(TestCase):

    def test_create_get(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        response = self.client.get(reverse('user-create'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/create-admin.html')

    def test_create_post(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        response = self.client.post(reverse('user-create'), {'username':'teste', 'email':'teste@gmail.com', 'password1':'ArthurTuring', 'password2':'ArthurTuring', 'is_superuser':False, 'is_staff':False})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('user-list'))

    def test_list(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        response = self.client.get(reverse('user-list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/list.html')

    def test_detail(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        response = self.client.get(reverse('user-detail', kwargs={'pk':1}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/detail.html')

    def test_update_get(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        response = self.client.get(reverse('user-update', kwargs={'pk':1}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/update.html')

    def test_update_post(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        response = self.client.post(reverse('user-update', kwargs={'pk': 1}), {'username':'teste1', 'email':'teste@gmail.com', 'password1':'ArthurTuring', 'password2':'ArthurTuring', 'is_superuser':False, 'is_staff':False})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('user-list'))

    def test_delete_get(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        response = self.client.get(reverse('user-delete', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/delete.html')

    def test_delete_post(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        response = self.client.post(reverse('user-delete', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('user-list'))
