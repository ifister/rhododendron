from django.conf.urls.defaults import *
from django.contrib import admin
from rhdday import settings



admin.autodiscover()



urlpatterns = patterns('',
    (r'^enterme/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)


if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns
    urlpatterns = patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns
    
    