# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20141031_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='favour',
            field=models.ManyToManyField(related_name='+', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
