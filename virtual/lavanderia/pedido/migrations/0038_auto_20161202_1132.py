# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 14:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0037_auto_20161202_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data_entrega',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
