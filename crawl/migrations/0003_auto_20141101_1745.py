# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawl', '0002_auto_20141101_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='temarticle',
            name='link',
            field=models.URLField(default='http://127.0.0.1:8000/admin/crawl/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temarticle',
            name='source_name',
            field=models.CharField(max_length=50, default='old'),
            preserve_default=False,
        ),
    ]
