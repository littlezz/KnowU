# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('headline', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('source_name', models.CharField(max_length=50)),
                ('link', models.URLField()),
                ('favour', models.ManyToManyField(related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookArticleMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('join_date', models.DateField(auto_now_add=True)),
                ('article', models.ForeignKey(to='main.Article')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('label', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('article_books', models.ManyToManyField(related_name='user_book', through='main.BookArticleMembership', blank=True, to='main.Article')),
                ('article_dislike', models.ManyToManyField(related_name='user_dislike', blank=True, to='main.Article')),
                ('article_history', models.ManyToManyField(related_name='user_history', blank=True, to='main.Article')),
                ('tags', models.ManyToManyField(blank=True, to='main.Tag')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='bookarticlemembership',
            name='userinfo',
            field=models.ForeignKey(to='main.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='main.Tag'),
            preserve_default=True,
        ),
    ]
