# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-07 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20170607_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='web_key',
            field=models.CharField(default='0xdveq', max_length=6, unique=True),
        ),
    ]
