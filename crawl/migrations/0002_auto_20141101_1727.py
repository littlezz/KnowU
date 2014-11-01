# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawl', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='xml',
            old_name='url',
            new_name='xml_url',
        ),
        migrations.AlterField(
            model_name='temarticle',
            name='tags',
            field=models.ManyToManyField(blank=True, to='crawl.TemTag'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='xml',
            name='tags',
            field=models.ManyToManyField(blank=True, to='crawl.TemTag'),
            preserve_default=True,
        ),
    ]
