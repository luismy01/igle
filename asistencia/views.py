
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import serializers
from django.core.urlresolvers import reverse
from django.utils import simplejson

from asistencia.models import asistencia

def redirect(urlname):
	return HttpResponseRedirect(reverse(urlname))

def home(request):
	return render_to_response("asistencia/grafico.html")

def list(request):
	
	if request.is_ajax():
		
		if request.method == "GET":

			models = []

			for model in asistencia.objects.all():
				models.append(model.dict())

			return HttpResponse(simplejson.dumps(models), mimetype='application/json')

		elif request.method == "POST":

			return save(request)

		else:

			return redirect("asistencia.home")

	else:
		
		return redirect("asistencia.home")

def save(request):
	
	model = asistencia()

	data = simplejson.loads(request.POST)
	print data

	return HttpResponse(simplejson.dumps(model.dict()), mimetype='application/json')

def delete(request):
	pass