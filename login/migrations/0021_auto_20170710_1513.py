# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-10 06:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0020_auto_20170707_1533'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='ActComment',
        ),
        migrations.AlterModelOptions(
            name='actcomment',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='bankbook',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.ActList'),
        ),
    ]
