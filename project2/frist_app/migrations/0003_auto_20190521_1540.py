# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-05-21 15:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frist_app', '0002_auto_20190520_2220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webpage',
            old_name='Topic',
            new_name='topic',
        ),
    ]
