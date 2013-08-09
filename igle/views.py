
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import asistencia
# Create your views here.

def home(request):
	return render_to_response("asistencia/grafico.html")
