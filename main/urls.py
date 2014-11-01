

__author__ = 'zz'

from django.conf.urls import patterns, include, url
from . import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'knowU.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^welcome/$', 'django.contrib.auth.views.login',{'template_name': 'welcome.html'}, name='welcome'),
    url(r'^register/$', views.Register.as_view(), name='register'),
    url(r'^manage/$', views.manage, name='manage'),
    url(r'^home/$', views.Home.as_view(), name='home'),
    url(r'^article/$', views.ajax_article, name='article'),
    url(r'^logout/$', views.userlogout, name='logout'),
    url(r'^book_or_favour_article/$', views.book_or_favour_article, name='book_or_favour'),
    url(r'^book_view/$', views.book_view, name='book_view'),

)
