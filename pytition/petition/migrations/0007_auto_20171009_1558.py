# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 13:58
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0006_auto_20171009_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petition',
            name='title',
            field=tinymce.models.HTMLField(),
        ),
    ]