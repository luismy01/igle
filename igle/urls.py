
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
<<<<<<< HEAD
from .views import MyTemplateView
=======
from igle.views import HomeView, LoginView, LogoutView
>>>>>>> b36aa02e3062eaea59fb43464d14c7812b1e4c0f

admin.autodiscover()

urlpatterns = patterns('',
<<<<<<< HEAD
    
    url(r'^$', 'igle.views.home', name='home'),
	url(r'^login/$', 'igle.views.userlogin', name='login'),
	url(r'^logout/$', 'igle.views.userlogout', name='logout'),

    url(r'^photo/(?P<identif>\d+)$', 'igle.views.photo', name='photo'),

    url(r'^personas/', include('personas.urls', namespace="personas", app_name="personas")),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^secretaria/', include('secretary.urls')),
    url(r'^template', MyTemplateView.as_view())
=======

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

>>>>>>> b36aa02e3062eaea59fb43464d14c7812b1e4c0f
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
    )
