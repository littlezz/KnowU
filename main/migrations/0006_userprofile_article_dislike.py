# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20141101_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='article_dislike',
            field=models.ManyToManyField(to='main.Article', blank=True, related_name='user_dislike'),
            preserve_default=True,
        ),
    ]
