# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-27 13:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import posts.utils
import posts.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=140, validators=[posts.validators.validate_content])),
                ('image', models.ImageField(blank=True, null=True, upload_to=posts.utils.generate_image_name)),
                ('privacy', models.CharField(choices=[('pb', 'Public'), ('pr', 'Private')], default='pb', max_length=2)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
