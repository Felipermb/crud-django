# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0004_auto_20161112_0625'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='nome_responsavel',
            field=models.CharField(default='felipe', max_length=200),
            preserve_default=False,
        ),
    ]
