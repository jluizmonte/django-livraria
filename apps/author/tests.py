from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from apps.author.models import Author
from apps.genre.models import Genre


class AuthorTest(TestCase):

    def test_create_get(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        response = self.client.get(reverse('author-create'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'author/create.html')

    def test_create_post(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        genre = Genre.objects.create(description='Romance', link='romance')
        self.client.force_login(user)
        response = self.client.post(reverse('author-create'), {'genre': genre.pk, 'name': 'Jane Doe'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('author-list'))

    def test_list(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        response = self.client.get(reverse('author-list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'author/list.html')

    def test_detail(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        Author.objects.create(name='Jane Doe')
        response = self.client.get(reverse('author-detail', kwargs={'pk':1}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'author/detail.html')

    def test_update_get(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        Author.objects.create(name='Jane Doe')
        response = self.client.get(reverse('author-update', kwargs={'pk':1}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'author/update.html')

    def test_update_post(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        Author.objects.create(name='Jane Doe')
        genre = Genre.objects.create(description='Romance', link='romance')
        response = self.client.post(reverse('author-update', kwargs={'pk': 1}), {'genre': genre.pk, 'name': 'Joe Doe'})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('author-list'))

    def test_delete_get(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        Author.objects.create(name='Jane Doe')
        response = self.client.get(reverse('author-delete', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'author/delete.html')

    def test_delete_post(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        Author.objects.create(name='Jane Doe')
        response = self.client.post(reverse('author-delete', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('author-list'))
