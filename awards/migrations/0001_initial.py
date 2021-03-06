# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-28 12:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, upload_to='images/')),
                ('bio', models.CharField(max_length=70)),
                ('contact', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(default=0, max_length=300)),
                ('landing_page', models.ImageField(blank=True, upload_to='landing_pages/')),
                ('usability', models.IntegerField(default=0)),
                ('design', models.IntegerField(default=0)),
                ('content', models.IntegerField(default=0)),
                ('link', models.CharField(blank=True, max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='awards.Project'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
