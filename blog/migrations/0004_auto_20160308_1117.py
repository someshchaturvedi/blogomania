# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-08 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160304_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_item',
            name='cog_id',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]