# Generated by Django 3.0 on 2019-12-16 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20191216_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='capa',
            field=models.ImageField(upload_to='capa/', verbose_name='Imagem da capa'),
        ),
    ]
