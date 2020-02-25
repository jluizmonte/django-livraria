from django.contrib.auth.models import User
from django.db import models
from apps.book.models import Book


class Item(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Livro')
    amount = models.IntegerField()

    def __str__(self):
        return self.book.name


class ShoppingCart(models.Model):
    class Meta:
        verbose_name = 'Carrinho de compras'
        verbose_name_plural = 'Carrinhos de compras'

    item = models.ManyToManyField(Item, verbose_name='Item')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')

    def __str__(self):
        return self.user.username
