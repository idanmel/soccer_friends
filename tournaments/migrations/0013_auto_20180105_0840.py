# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-05 08:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0012_auto_20171231_1942'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='match',
            unique_together=set([('stage', 'home_team', 'away_team')]),
        ),
    ]
