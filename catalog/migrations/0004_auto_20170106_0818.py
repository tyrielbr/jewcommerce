# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, max_length=60, verbose_name='Descrição curta'),
        ),
    ]
