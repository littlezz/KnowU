from django.conf.urls import patterns, include, url
from django.contrib import admin
import crawl.urls
import main.urls
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'knowU.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', include(main.urls)),
    url(r'^crawl/', include(crawl.urls)),
)
