
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('asistencia.views',
    #url(r'^$', 'inicio'),
    url(r'^$', TemplateView.as_view(template_name='asistencia/grafico.html'), name="asistencia.home"),
    url(r'^list$', 'list', name="asistencia.list"),
    #url(r'^save$', 'save', name="asistencia.save"),
    #url(r'^delete$', 'delete', name="asistencia.delete"),
)