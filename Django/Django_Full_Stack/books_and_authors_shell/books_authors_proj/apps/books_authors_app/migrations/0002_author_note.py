# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-17 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='note',
            field=models.TextField(default='N/A'),
            preserve_default=False,
        ),
    ]