from django.contrib.auth.models import User
from django.db import models
from apps.book.models import Book


class ShoppingCart(models.Model):
    class Meta:
        verbose_name = 'Carrinho de compras'
        verbose_name_plural = 'Carrinhos de compras'

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    book = models.ManyToManyField(Book, verbose_name='Livro')

    def __str__(self):
        return self.user.username
