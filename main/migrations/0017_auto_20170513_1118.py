# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 11:18
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_cbtag_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cbtag',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, default=None, editable=False, max_length=200, populate_from='name'),
            preserve_default=False,
        ),
    ]
