	
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils import simplejson
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView, TemplateView
import json

from asistencia.models import Asistencia

TEMPLATE_ASISTENCIA = "asistencia/asistencia.html"
TEMPLATE_LISTADO = "asistencia/listado.html"
TEMPLATE_GRAFICO = "asistencia/grafico.html"


class InicioView(TemplateView):
	
	template_name = TEMPLATE_GRAFICO

class CrearAsistenciaView(CreateView):
	
	model = Asistencia
	success_url = reverse_lazy('listar_asistencia')
	template_name = TEMPLATE_ASISTENCIA

class EditarAsistenciaView(UpdateView):
	
	context_object_name = "asistencia"
	model = Asistencia
	success_url = reverse_lazy('listar_asistencia')
	template_name = TEMPLATE_ASISTENCIA

	def get_context_data(self, **kwargs):
		context = super(EditarAsistenciaView, self).get_context_data(**kwargs)
		context['editar'] = True
		return context


class BorrarAsistenciaView(DeleteView):
	
	model = Asistencia
	success_url = reverse_lazy('listar_asistencia')

	def get(self, request, *args, **kwargs):
		return self.post(self, request, args, kwargs)


class ListarAsistenciaView(ListView):
	
	context_object_name = "asistencias"
	model = Asistencia
	queryset = Asistencia.objects.order_by('-fecha')
	template_name = TEMPLATE_LISTADO

class AjaxAsistenciaView(ListView):
	
	model = Asistencia
	
	def get(self, request, *args, **kwargs):
		ini = 0
		fin = 10

		if 'ini' in request.GET:
			ini = int(request.GET["ini"])

		if 'fin' in request.GET:
			fin = int(request.GET["fin"])

		registros = Asistencia.objects.order_by('-fecha')[ini:fin]
		json_list = [ r.dict() for r in registros ]

		for i in range(len(json_list)):
			json_list[i]['counter'] = ini + (i+1)

		return HttpResponse(json.dumps({"data": json_list}), content_type = 'application/json')


