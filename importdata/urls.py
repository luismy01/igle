from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('importdata.views',
	url(r'^$', 'import_view', name="import_view"),
)
