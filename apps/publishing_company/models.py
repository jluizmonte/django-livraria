from django.db import models


class PublishingCompany(models.Model):
    class Meta:
        verbose_name = "Editora"
        verbose_name_plural = 'Editoras'

    name = models.CharField(max_length=200, verbose_name="Nome")

    def __str__(self):
        return self.name
