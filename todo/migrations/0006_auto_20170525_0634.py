# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20170524_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='completed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
