# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-13 08:49
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_auto_20161012_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouse',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='a', editable=False, populate_from='item', unique_with=('trans_in',)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='trans_in',
            field=models.DateField(verbose_name='\u5165\u5e93\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='trans_out',
            field=models.DateField(blank=True, null=True, verbose_name='\u51fa\u5e93\u65f6\u95f4'),
        ),
    ]