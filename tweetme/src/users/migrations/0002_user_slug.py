# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-24 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(default=None, null=True),
        ),
    ]
