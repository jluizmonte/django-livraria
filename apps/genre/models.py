from django.db import models


class Genre(models.Model):
    class Meta:
        verbose_name_plural = 'Gênero'

    descricao = models.CharField(verbose_name='Descrição', max_length=50)

    def __str__(self):
        return self.descricao