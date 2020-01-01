from django.db import models

from apps.genre.models import Genre


class Author(models.Model):
    class Meta:
        verbose_name_plural = "Autores"
        verbose_name = "Autor"

    name = models.CharField(max_length=100, verbose_name="Nome")
    genre = models.ManyToManyField(Genre, verbose_name='Gênero')

    def __str__(self):
        return self.name
