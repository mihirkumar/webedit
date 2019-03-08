# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-20 17:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0032_auto_20180420_1040'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['-lastUpdated', 'title']},
        ),
        migrations.AlterField(
            model_name='page',
            name='webKey',
            field=models.CharField(blank=True, default='', max_length=32),
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([('user', 'slug')]),
        ),
    ]
