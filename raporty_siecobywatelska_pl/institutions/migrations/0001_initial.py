# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-05 05:33
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teryt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True, verbose_name='Slug')),
                ('regon', models.CharField(blank=True, max_length=14, null=True, unique=True, verbose_name='REGON number')),
                ('email', models.EmailField(max_length=254, verbose_name='Email of institution')),
                ('jst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teryt.JST', verbose_name='Unit of administrative division')),
                ('parents', models.ManyToManyField(blank=True, related_name='_institution_parents_+', to='institutions.Institution', verbose_name='Parent institutions')),
            ],
            options={
                'verbose_name': 'Institution',
                'verbose_name_plural': 'Institution',
                'ordering': ['name'],
            },
        ),
    ]
