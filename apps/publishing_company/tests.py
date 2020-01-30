from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import PublishingCompany


class GenreTest(TestCase):

    def test_create_get(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        response = self.client.get(reverse('publishing-company-create'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'publishing_company/create.html')

    def test_create_post(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        response = self.client.post(reverse('publishing-company-create'), {'name':'teste'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('publishing-company-list'))

    def test_list(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        response = self.client.get(reverse('publishing-company-list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'publishing_company/list.html')

    def test_detail(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        PublishingCompany.objects.create(name='Teste')
        response = self.client.get(reverse('publishing-company-detail', kwargs={'pk':1}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'publishing_company/detail.html')

    def test_update_get(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        PublishingCompany.objects.create(name='Teste')
        response = self.client.get(reverse('publishing-company-update', kwargs={'pk':1}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'publishing_company/update.html')

    def test_update_post(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        PublishingCompany.objects.create(name='Teste')
        response = self.client.post(reverse('publishing-company-update', kwargs={'pk': 1}), {'name':'teste 1'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('publishing-company-list'))

    def test_delete_get(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        PublishingCompany.objects.create(name='Teste')
        response = self.client.get(reverse('publishing-company-delete', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'publishing_company/delete.html')

    def test_delete_post(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        PublishingCompany.objects.create(name='Teste')
        response = self.client.post(reverse('publishing-company-delete', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('publishing-company-list'))
