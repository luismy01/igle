
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from igle.views import home

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', home, name='inicio'),
	url(r'^asistencia/', include('asistencia.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^entrar', 'igle.views.entrar', name='entrar'),
    url(r'^salir', 'igle.views.salir', name='salir'),
)

urlpatterns += patterns('',
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
    )
