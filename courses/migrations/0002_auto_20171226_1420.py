# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-26 08:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cbcoursestags',
            name='courses',
        ),
        migrations.RemoveField(
            model_name='cbcoursestags',
            name='tag',
        ),
        migrations.AlterModelTable(
            name='cbcourses',
            table='cb_courses_tags',
        ),
        migrations.DeleteModel(
            name='CbCoursesTags',
        ),
    ]
