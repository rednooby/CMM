# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 05:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_actlist_actnum'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actlist',
            old_name='actId',
            new_name='act',
        ),
        migrations.RenameField(
            model_name='actlist',
            old_name='actInfo',
            new_name='act_info',
        ),
        migrations.RenameField(
            model_name='actlist',
            old_name='actName',
            new_name='act_name',
        ),
        migrations.RenameField(
            model_name='actlist',
            old_name='actNum',
            new_name='act_num',
        ),
        migrations.RenameField(
            model_name='actlist',
            old_name='actSummary',
            new_name='act_summary',
        ),
    ]
