# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-24 19:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20161223_1953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-timestamp'], 'verbose_name_plural': 'Posts'},
        ),
    ]
