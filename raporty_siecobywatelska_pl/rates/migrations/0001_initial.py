# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 05:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institutions', '0001_initial'),
        ('questionnaire', '0001_initial'),
        ('ranking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstitutionGroupRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_points', models.IntegerField(verbose_name='Total points')),
                ('collected_points', models.IntegerField(verbose_name='Collected points')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='questionnaire.Group')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups_rates', to='institutions.Institution')),
            ],
            options={
                'verbose_name_plural': 'Institutions assessments',
                'verbose_name': "Groups's rates",
            },
        ),
        migrations.CreateModel(
            name='InstitutionRankingRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_points', models.IntegerField(verbose_name='Total points')),
                ('collected_points', models.IntegerField(verbose_name='Collected points')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ranking_rates', to='institutions.Institution')),
                ('ranking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='ranking.Ranking')),
            ],
            options={
                'verbose_name_plural': 'Institutions rates',
                'verbose_name': "Institution's rate",
            },
        ),
        migrations.AlterUniqueTogether(
            name='institutionrankingrate',
            unique_together=set([('institution', 'ranking')]),
        ),
        migrations.AlterUniqueTogether(
            name='institutiongrouprate',
            unique_together=set([('institution', 'group')]),
        ),
    ]