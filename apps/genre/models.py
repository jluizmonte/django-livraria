from django.db import models


class Genre(models.Model):
    class Meta:
        verbose_name_plural = 'Gênero'

    description = models.CharField(verbose_name='Descrição', max_length=50, unique=True)
    link = models.SlugField(verbose_name='Link', max_length=50, unique=True)

    def __str__(self):
        return self.description
