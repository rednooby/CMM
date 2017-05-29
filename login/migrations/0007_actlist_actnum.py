# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_remove_actlist_actnum'),
    ]

    operations = [
        migrations.AddField(
            model_name='actlist',
            name='actNum',
            field=models.CharField(default=-4444, max_length=15, unique=True, verbose_name='계좌번호'),
            preserve_default=False,
        ),
    ]