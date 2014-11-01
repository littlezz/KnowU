# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_article_favor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookarticlemembership',
            old_name='user',
            new_name='userinfo',
        ),
        migrations.RemoveField(
            model_name='article',
            name='favor',
        ),
        migrations.AddField(
            model_name='article',
            name='favour',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
