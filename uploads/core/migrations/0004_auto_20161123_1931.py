# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-23 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_sprite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sprite',
            name='image',
            field=models.ImageField(upload_to='sprites/'),
        ),
    ]
