# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-10 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0018_match_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='away_goals',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_goals',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]