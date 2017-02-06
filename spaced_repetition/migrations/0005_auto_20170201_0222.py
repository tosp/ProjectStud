# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-01 02:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spaced_repetition', '0004_auto_20170201_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='user_profiles.Student'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='parent_directory',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='spaced_repetition.Folder'),
        ),
    ]
