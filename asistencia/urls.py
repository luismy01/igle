from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from views import InicioView, CrearAsistenciaView, EditarAsistenciaView, BorrarAsistenciaView, ListarAsistenciaView, AjaxAsistenciaView

urlpatterns = patterns('asistencia.views',
    
    # home
	url(r'^$', InicioView.as_view(), name="home_asistencia"),

	# add
	url(r'^agregar$', login_required(CrearAsistenciaView.as_view()), name="agregar_asistencia"),
	url(r'^add$', login_required(CrearAsistenciaView.as_view()), name="asistencia_add"),
	url(r'^new$', login_required(CrearAsistenciaView.as_view()), name="asistencia_new"),

	# edit
	url(r'^(?P<pk>[\d]+)$', login_required(EditarAsistenciaView.as_view()), name="asistencia_view_id"),
	url(r'^(?P<pk>[\d]+)/edit$', login_required(EditarAsistenciaView.as_view()), name="asistencia_edit"),

	# delete
	url(r'^(?P<pk>\d+)/borrar$', login_required(BorrarAsistenciaView.as_view()), name="borrar_asistencia"),
	url(r'^(?P<pk>\d+)/delete$', login_required(BorrarAsistenciaView.as_view()), name="asistencia_delete"),

	# list
	url(r'^listar$', login_required(ListarAsistenciaView.as_view()), name="listar_asistencia"),
	url(r'^listado$', login_required(ListarAsistenciaView.as_view()), name="listado_asistencia"),
	url(r'^list$', login_required(ListarAsistenciaView.as_view()), name="asistencia_list"),

	# graph
	url(r'^grafico$', InicioView.as_view(), name="grafico_asistencia"),
	url(r'^graph$', InicioView.as_view(), name="asistencia_graph"),

	# ajax data
	url(r'^ajax$', login_required(AjaxAsistenciaView.as_view()), name="asistencia_ajax"),
	
)
