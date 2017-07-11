# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-11 04:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0026_auto_20170710_1939'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='bankbook',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.ActList'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
