from django.db import models

from apps.author.models import Author
from apps.genre.models import Genre
from apps.publishing_company.models import PublishingCompany


class Book(models.Model):
    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'

    publishing_company = models.ManyToManyField(PublishingCompany, verbose_name='Editora')
    genre = models.ManyToManyField(Genre, verbose_name='Gênero')
    author = models.ManyToManyField(Author, verbose_name="Autor")
    name = models.CharField(max_length=200, verbose_name="Nome")
    description = models.TextField(verbose_name='Descrição')
    capa = models.ImageField(verbose_name='Imagem da capa', upload_to='capa/')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Preço")

    def __str__(self):
        return self.name
