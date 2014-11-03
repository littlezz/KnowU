# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_userprofile_article_dislike'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagAssign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tags', models.ManyToManyField(to='main.Tag')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
