# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-05-20 22:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frist_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webpage',
            old_name='top_name',
            new_name='name',
        ),
    ]
