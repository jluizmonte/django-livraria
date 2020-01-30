from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from apps.author.models import Author
from apps.genre.models import Genre
from apps.publishing_company.models import PublishingCompany
from .models import Book
from django.core.files.uploadedfile import SimpleUploadedFile


class BookTest(TestCase):
    testfile = (
        b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04'
        b'\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02'
        b'\x02\x4c\x01\x00\x3b'
    )
    image = SimpleUploadedFile('small.gif', testfile, content_type='image/gif')

    def test_create_get(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        response = self.client.get(reverse('book-create'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/create.html')

    def test_create_post(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        genre = Genre.objects.create(description='Romance', link='romance')
        author = Author.objects.create(name='Jane Doe')
        publishing_company = PublishingCompany.objects.create(name='Verification')
        self.client.force_login(user)
        response = self.client.post(reverse('book-create'), {
            'author':author.pk, 'genre':genre.pk,
            'name':'Verification', 'description':'A functionality test', 'publishing_company':publishing_company.pk,
            'price':10, 'book_cover':self.image
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('book-list'))

    def test_list(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        response = self.client.get(reverse('book-list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/list.html')

    def test_detail(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        Book.objects.create(name='Jane Doe', description='teste', price=10, book_cover=self.image)
        response = self.client.get(reverse('book-detail', kwargs={'pk':1}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/detail.html')

    def test_update_get(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        Book.objects.create(name='Jane Doe', description='teste', price=10, book_cover=self.image)
        response = self.client.get(reverse('book-update', kwargs={'pk':1}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/update.html')

    def test_update_post(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        genre = Genre.objects.create(description='Romance', link='romance')
        author = Author.objects.create(name='Jane Doe')
        publishing_company = PublishingCompany.objects.create(name='Verification')
        Book.objects.create(name='Jane Doe', description='teste', price=10, book_cover=self.image)
        response = self.client.post(reverse('book-update', kwargs={'pk': 1}), {'name':'teste', 'description':'teste',
                                                                               'price':10,'genre':genre.pk, 'author':author.pk,
                                                                               'publishing_company':publishing_company.pk})
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('book-list'))

    def test_delete_get(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        Book.objects.create(name='Jane Doe', description='teste', price=10, book_cover=self.image)
        response = self.client.get(reverse('book-delete', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/delete.html')

    def test_delete_post(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com', is_superuser=True)
        self.client.force_login(user)
        Book.objects.create(name='Jane Doe', description='teste', price=10, book_cover=self.image)
        response = self.client.post(reverse('book-delete', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, reverse('book-list'))