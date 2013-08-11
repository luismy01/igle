
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import serializers
from django.core.urlresolvers import reverse
from django.utils import simplejson

from asistencia.models import asistencia

def redirect(urlname):
	return HttpResponseRedirect(reverse(urlname))

def render(request, template):
	return render_to_response(template, context_instance=RequestContext(request))

def home(request):
	
	if request.is_ajax():
		
		# list all asistencias
		if request.method == "GET":

			return list(request)

		# save a new asistencia
		elif request.method == "POST":

			return save(request)

		else:

			return render(request, "asistencia/grafico.html")


	else:
		
		return render(request, "asistencia/grafico.html")


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
		
		# delete one asistencia
		if request.method == "DELETE":

			return deleteID(request, id)

		else:

			return render(request, "asistencia/grafico.html")

	else:
		
		return render(request, "asistencia/grafico.html")



def save(request):
	
	model = asistencia()

	for key in request.POST:
		data = simplejson.loads(key)
		break

	model.fecha = data["fecha"]
	model.hermanos = data["hermanos"]
	model.visitas = data["visitas"]
	model.ninos = data["ninos"]
	model.adolescentes = data["adolescentes"]
	model.ofrenda = data["ofrenda"]
	model.observaciones = data["observaciones"]	

	model.save();

	return HttpResponse(simplejson.dumps(model.dict()), mimetype='application/json')

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
	
	model = asistencia.objects.get(fecha=fecha)
	return HttpResponse(simplejson.dumps(model.dict()), mimetype='application/json')



def selectID(request, id):

	model = asistencia.objects.get(id=str(id))
	return HttpResponse(simplejson.dumps(model.dict()), mimetype='application/json')



def list(request):
	
	models = []
	for model in asistencia.objects.all().order_by("fecha"):
		models.append(model.dict())

	return HttpResponse(simplejson.dumps(models), mimetype='application/json')