# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-18 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180617_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foundperson',
            name='FoundPersonImage',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='missingperson',
            name='MissingPersonImage',
            field=models.ImageField(upload_to=''),
        ),
    ]
