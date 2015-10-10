
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

from .views import MyTemplateView, MyFormView

admin.autodiscover()

urlpatterns = patterns('',
					   url(r'^$', 'igle.views.home', name='home'),
					   url(r'^login/$', 'igle.views.userlogin', name='login'),
					   url(r'^logout/$', 'igle.views.userlogout', name='logout'),
					   #url(r'^photo/(?P<identif>\d+)$', 'igle.views.photo', name='photo'),
					   url(r'^form/$', MyFormView.as_view(), name='myformview'),
					   
					   url(r'^personas/', include('personas.urls', namespace="personas", app_name="personas")),
					   
					   url(r'^admin/', include(admin.site.urls)),
					   #url(r'^secretaria/', include('secretary.urls')),
					   url(r'^template', MyTemplateView.as_view()),
					   url(r'^admin/', include(admin.site.urls)),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
    )
