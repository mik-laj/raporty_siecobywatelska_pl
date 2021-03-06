# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-06 18:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_textoption'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('answers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='note',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='value',
        ),
        migrations.AddField(
            model_name='answer',
            name='option',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='questionnaire.TextOption'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
