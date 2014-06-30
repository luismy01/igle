
import os.path
from django.http import HttpResponse
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

from secretary.models import Miembro

def isset(request, param):
	
	if request.method == 'GET' and param in request.GET:
		return True
	elif request.method == 'POST' and param in request.POST:
		return True
	else:
		return False

def get(request, param):
	
	if request.method == 'GET' and param in request.GET:
		return request.GET[param]
	elif request.method == 'POST' and param in request.POST:
		return request.POST[param]
	else:
		return None


# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def listar_miembros(request):

    return render_to_response("website/secretary/list-members.html",
							{'user': request.user, 'settings': settings}
							, context_instance=RequestContext(request))

@login_required(login_url=settings.LOGIN_URL)
def buscar_miembros(request):

    text = "" if not isset(request, "q") else get(request, "q")
    top = 15 if not isset(request, "top") else get(request, "top")
        
    miembros = Miembro.objects.filter(
        Q(identificacion__icontains = text) | Q(nombres__icontains = text) | Q(apellidos__icontains = text)
    ).order_by('nombres', 'apellidos')[:top]
    
    html = u""
    template = u"""
        <li>
            <a href="{0}?member={1}" title="{2}">
                <img src="{3}images/fotos/{4}" alt="{2}" />
            </a>
        </li>
    """

    for member in miembros:
        
        foto = member.identificacion + ".JPG"               
        if not os.path.isfile(settings.STATICFILES_DIRS[0] + "images/fotos/" + foto):
            foto = "fotoM.png" if member.genero == "M" else "fotoF.png"
             
        html += template.format(settings.REPORT_URL, member.identificacion, member.nombres, settings.STATIC_URL, foto)
            
    return HttpResponse(html)

