# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20141031_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='link',
            field=models.URLField(default='http://127.0.0.1:8000/app/welcome/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='source_name',
            field=models.CharField(default='old', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='headline',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='label',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
