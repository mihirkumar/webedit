# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-17 15:28
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0026_auto_20171016_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='assignment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='page',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='page',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pages', to=settings.AUTH_USER_MODEL),
        ),
    ]
