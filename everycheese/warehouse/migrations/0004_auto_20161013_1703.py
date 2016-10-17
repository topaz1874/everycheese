# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-13 09:03
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0003_auto_20161013_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouse',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='item_name', unique_with=('item_name', 'trans_in')),
        ),
    ]
