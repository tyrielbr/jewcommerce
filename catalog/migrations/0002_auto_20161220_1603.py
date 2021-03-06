# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, max_length=150, verbose_name='Descrição curta'),
        ),
    ]
