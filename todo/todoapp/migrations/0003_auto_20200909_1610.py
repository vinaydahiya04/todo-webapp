# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-09-09 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20200909_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='target_date',
            field=models.DateField(),
        ),
    ]
