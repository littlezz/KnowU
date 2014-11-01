__author__ = 'zz'
from django.conf.urls import patterns, include, url
from . import views
urlpatterns = patterns('',


    url(r'^list/$', views.List.as_view(), name='list'),
    url(r'^commit_article', views.every_article_commit_and_clear, name='every_article_commit_and_clear')
)
