# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-27 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
