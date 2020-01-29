from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Genre


class GenreTest(TestCase):

    def test_create_get(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        response = self.client.get(reverse('genre-create'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'genre/create.html')

    def test_create_post(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        response = self.client.post(reverse('genre-create'), {'description':'teste', 'link':'teste'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('genre-list-admin'))

    def test_list(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        response = self.client.get(reverse('genre-list-admin'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'genre/list.html')

    def test_detail(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        Genre.objects.create(description='Teste', link='teste')
        response = self.client.get(reverse('genre-detail', kwargs={'pk':1}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'genre/detail.html')

    def test_update_get(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        Genre.objects.create(description='Teste', link='teste')
        response = self.client.get(reverse('genre-update', kwargs={'pk':1}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'genre/update.html')

    def test_update_post(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        Genre.objects.create(description='Romance', link='romance')
        response = self.client.post(reverse('genre-update', kwargs={'pk': 1}), {'description':'Romance 1', 'link':'romance'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('genre-list-admin'))

    def test_delete_get(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        Genre.objects.create(description='Romance', link='romance')
        response = self.client.get(reverse('genre-delete', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'genre/delete.html')

    def test_delete_post(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        Genre.objects.create(description='Romance', link='romance')
        response = self.client.post(reverse('genre-delete', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('genre-list-admin'))

    def test_api_list(self):
        Genre.objects.create(description='Romance', link='romance')
        response = self.client.get(reverse('genre-list'))
        self.assertEquals(response.status_code, 200)
