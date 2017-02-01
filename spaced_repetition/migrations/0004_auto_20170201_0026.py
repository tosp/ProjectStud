# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-01 00:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spaced_repetition', '0003_auto_20170120_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='owner',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='user_profiles.Student'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='parent_directory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spaced_repetition.Folder'),
        ),
    ]