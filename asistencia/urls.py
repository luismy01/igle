from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('asistencia.views',
    
	url(r'^$', 'home', name="home_asistencia"),
	url(r'^agregar$', 'agregar', name="agregar_asistencia"),
	url(r'^editar$', 'editar', name="editar_asistencia"),
	url(r'^grafico$', 'home', name="grafico_asistencia"),
	
    url(r'^(\d+)$', 'manageID', name="asistencia.manageID"),
    url(r'^(\d{4}-\d{2}-\d{2})$', 'manage', name="asistencia.manage"),
)
