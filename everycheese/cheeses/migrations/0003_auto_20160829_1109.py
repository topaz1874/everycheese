# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-29 03:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cheeses', '0002_cheese_country_of_orgin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cheese',
            old_name='country_of_orgin',
            new_name='country_of_origin',
        ),
    ]
