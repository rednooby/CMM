# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-11 05:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0028_auto_20170711_1406'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='bankbook',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.ActList'),
        ),
    ]