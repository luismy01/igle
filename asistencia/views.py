	
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.urlresolvers import reverse
from django.utils import simplejson
from django.views.generic.detail import DetailView
import json

from asistencia.models import Asistencia

TEMPLATE_ASISTENCIA = "asistencia/asistencia.html"
TEMPLATE_LISTADO = "asistencia/listado.html"
TEMPLATE_GRAFICO = "asistencia/grafico.html"


def render(request, template, dictionary=None):
	return render_to_response(template, dictionary, context_instance=RequestContext(request))

def home(request):
	
	if request.is_ajax():
		
		# list all asistencias
		if request.method == "GET":

			return list(request)

		# save a new asistencia
		elif request.method == "POST":

			return save(request)

		else:

			return render(request, TEMPLATE_GRAFICO)

	else:
		
		return render(request, TEMPLATE_GRAFICO)

def guardar(request):

	if request.method == "POST":
		
		model = Asistencia()
		data = request.POST

		model.id = data["id"]
		model.fecha = data["fecha"]
		model.hermanos = data["hermanos"]
		model.visitas = data["visitas"]
		model.ninos = data["ninos"]
		model.adolescentes = data["adolescentes"]
		model.ofrenda = data["ofrenda"]
		model.observaciones = data["observaciones"]	
		
		print model

		model.save();
		return True

	return False

@login_required
def agregar_view(request):

	if request.method == "POST":
		
		model = Asistencia()
		data = request.POST

		model.fecha = data["fecha"]
		model.hermanos = data["hermanos"]
		model.visitas = data["visitas"]
		model.ninos = data["ninos"]
		model.adolescentes = data["adolescentes"]
		model.ofrenda = data["ofrenda"]
		model.observaciones = data["observaciones"]	
	
		model.save();
	
		return redirect("/asistencia")
	
	return render(request, TEMPLATE_ASISTENCIA)

@login_required
def editar_view(request, id=0):

	if request.method == "POST":

		if guardar(request) == True:
			return redirect("/asistencia/listar")

	elif request.method == "GET" and id != 0:

		item = Asistencia.objects.get(id=id)
		return render(request, TEMPLATE_ASISTENCIA, {
			"asistencia": item,
			"editar": True
		})

	else:

		return redirect("/asistencia/agregar")

@login_required
def borrar_view(request, id):

	model = Asistencia()
	model.id = id
	model.delete()
	return redirect("/asistencia/listar")

def listar(request):

	page = 1
	rows = 2048

	if 'page' in request.GET:
		page = int(request.GET['page'])

	if 'rows' in request.GET:
		rows = int(request.GET["rows"])

	ini = ((page-1) * rows)
	fin = ini + rows

	#registros = Asistencia.objects.order_by('-fecha')[ini:fin]
	registros = Asistencia.objects.order_by('-fecha')

	if request.is_ajax():

		json_list = [ r.dict() for r in registros ]

		for i in range(len(json_list)):
			json_list[i]['counter'] = ini + (i+1)

		return HttpResponse(json.dumps({"data": json_list}), content_type = 'application/json')

	return render(request, TEMPLATE_LISTADO, {
		"asistencias": registros
	})

def ajax(request):
	
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










def manage(request, fecha):

	if request.is_ajax():
		
		# select one asistencia
		if request.method == "GET":

			return select(request, fecha)

		# delete one asistencia
		elif request.method == "DELETE":

			return delete(request, fecha)

		else:

			return render(request, "asistencia/grafico.html")


	else:
		
		return render(request, "asistencia/grafico.html")

def manageID(request, id):

	# select one asistencia
	if request.method == "GET":

		return selectID(request, id)

	if request.is_ajax():
		
		# update one asistencia
		if request.method in ("PUT", "POST"):

			return save(request)

		# delete one asistencia
		if request.method == "DELETE":

			return deleteID(request, id)

		else:

			return render(request, "asistencia/grafico.html")

	else:
		
		return render(request, "asistencia/grafico.html")

def delete(request, fecha):
	
	model = asistencia()
	model.fecha = fecha

	model.delete()

	return HttpResponse(simplejson.dumps(model.dict()), mimetype='application/json')

def deleteID(request, id):
	
	model = asistencia()
	model.id = str(id)

	model.delete()

	return HttpResponse(simplejson.dumps(model.dict()), mimetype='application/json')

def select(request, fecha):
	
	model = Asistencia.objects.get(fecha=fecha)
	return HttpResponse(simplejson.dumps(model.dict()), mimetype='application/json')

def selectID(request, id):

	model = Asistencia.objects.get(id=str(id))
	return HttpResponse(simplejson.dumps(model.dict()), mimetype='application/json')

def list(request):
	
	models = []
	for model in Asistencia.objects.all().order_by("fecha"):
		models.append(model.dict())

	return HttpResponse(simplejson.dumps(models), mimetype='application/json')


class AsistenciaView(DetailView):
	model = Asistencia
	context_object_name = "asistencia"
	def get_template_names(self):
		return TEMPLATE_ASISTENCIA
