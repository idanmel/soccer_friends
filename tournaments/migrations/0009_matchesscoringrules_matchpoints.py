# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-31 19:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tournaments', '0008_auto_20171230_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchesScoringRules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precise', models.PositiveSmallIntegerField(default=0)),
                ('imprecise', models.PositiveSmallIntegerField(default=0)),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Stage')),
            ],
        ),
        migrations.CreateModel(
            name='MatchPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.PositiveSmallIntegerField(default=None)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Match')),
            ],
        ),
    ]
