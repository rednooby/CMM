# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-30 03:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_auto_20170627_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankbook',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.ActList'),
        ),
    ]
