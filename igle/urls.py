
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from igle.views import HomeView, LoginView, LogoutView

admin.autodiscover()

urlpatterns = patterns('',

    # igle app urls
	url(r'^$', HomeView.as_view(), name='inicio'),
    url(r'^ipuc/$', HomeView.as_view(), name='inicio'),
    url(r'^entrar$', LoginView.as_view(), name='entrar'),
    url(r'^salir$', LogoutView.as_view(), name='salir'),

    # importdata app urls
    url(r'^importdata', 'importdata.views.import_view', name='importdata'),

    # asistencia app urls
    url(r'^ipuc/asistencia/', include('asistencia.urls')),
    url(r'^admin/', include(admin.site.urls)),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
    )
