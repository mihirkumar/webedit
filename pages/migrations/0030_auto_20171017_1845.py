# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-17 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0029_auto_20171017_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]
