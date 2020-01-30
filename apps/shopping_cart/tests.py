from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from apps.book.models import Book
from .models import ShoppingCart


class UserTest(TestCase):

    def test_add(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com')
        self.client.force_login(user)
        book = Book.objects.create(name='Jane Doe', description='teste', price=10)
        response = self.client.get(reverse('shopping-cart-add', kwargs={'book':book.pk}))
        ShoppingCart.objects.get(user=user)
        self.assertEquals(response.status_code, 302)

    def test_remove(self):
        user = User.objects.create(username='joedoe', password='ArthurTuring', email='joedoe@admin.com')
        self.client.force_login(user)
        book = Book.objects.create(name='Jane Doe', description='teste', price=10)
        shopping_cart = ShoppingCart.objects.create(user=user)
        shopping_cart.book.add(book)
        response = self.client.get(reverse('shopping-cart-remove', kwargs={'book': book.pk}))
        ShoppingCart.objects.get(user=user)
        self.assertEquals(response.status_code, 302)