# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-13 02:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=50, unique=True)),
                ('ip', models.GenericIPAddressField(unique=True)),
                ('port', models.IntegerField(default='22')),
                ('os', models.CharField(default='linux', max_length=20, verbose_name='Operating System')),
            ],
        ),
    ]
