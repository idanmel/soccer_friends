# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-30 20:11
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tournaments', '0007_match'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchPrediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_goals', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('away_goals', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='match',
            name='away_goals',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_goals',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='matchprediction',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournaments.Match'),
        ),
    ]
