# Generated by Django 3.0.2 on 2020-01-27 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genre', '0004_auto_20200109_0238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='descricao',
            new_name='description',
        ),
    ]