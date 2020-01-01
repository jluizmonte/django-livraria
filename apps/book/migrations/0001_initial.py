# Generated by Django 3.0 on 2019-12-16 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genre', '0001_initial'),
        ('author', '0002_auto_20191215_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('author', models.ManyToManyField(to='author.Author', verbose_name='Autor')),
                ('genre', models.ManyToManyField(to='genre.Genre', verbose_name='Gênero')),
            ],
            options={
                'verbose_name': 'Livro',
                'verbose_name_plural': 'Livros',
            },
        ),
    ]
