# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 02:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20170526_1130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actlist',
            name='actNum',
        ),
    ]