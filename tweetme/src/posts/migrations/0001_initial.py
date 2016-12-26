# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-23 15:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import posts.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=140, validators=[posts.utils.validate_content])),
                ('image', models.ImageField(default=None, upload_to=posts.utils.generate_imagename)),
                ('privacy', models.CharField(choices=[('pb', 'Public'), ('pr', 'Private')], default='pb', max_length=2)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='posts',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='posts.Posts'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]