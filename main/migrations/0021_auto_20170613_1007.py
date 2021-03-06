# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-13 10:07
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20170601_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cbcategory',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='name', unique=True),
        ),
        migrations.AlterField(
            model_name='cbquestion',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='cbtag',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='name', unique=True),
        ),
        migrations.AlterField(
            model_name='cbtopic',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title', unique=True),
        ),
    ]
