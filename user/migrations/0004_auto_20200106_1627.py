# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-06 16:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='only_matche',
            new_name='only_matched',
        ),
    ]