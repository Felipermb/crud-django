# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 14:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0035_auto_20161202_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data_entrega',
            field=models.DateField(default=datetime.datetime(2016, 12, 4, 11, 31, 45, 459140)),
        ),
    ]
