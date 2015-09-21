
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import os.path

from secretary.models import Miembro

@login_required(login_url=settings.LOGIN_URL)
def home(request):
	return HttpResponsePermanentRedirect("/secretaria/list-members")


def userlogin(request):

	if request.method == 'GET':
		return render_to_response("website/login.html",
			{'msg': u'[ESTADO]'},
			RequestContext(request)
		)

	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect(reverse("home"))
	
	return render_to_response("website/login.html",
		{'msg': u'Su usuario y clave no coinciden. Por favor intente de nuevo.'},
		RequestContext(request)
	)


@login_required(login_url=settings.LOGIN_URL)
def userlogout(request):

	logout(request)
	return HttpResponseRedirect(reverse("login"))


@login_required(login_url=settings.LOGIN_URL)
def photo(request, identif):
	
	try:	
	
		member = Miembro.objects.get(identificacion=identif)
		foto = member.identificacion + ".JPG"
		
		if not os.path.isfile(settings.STATICFILES_DIRS[0] + "images/fotos/" + foto):
			foto = "fotoM.png" if member.genero == "M" else "fotoF.png"
	
	except Miembro.DoesNotExist:
		foto = "fotoM.png"
	
	f = open(settings.STATICFILES_DIRS[0] + "images/fotos/" + foto)
	
	response = HttpResponse("", content_type="image/jpeg")
	response.write(f.read())	
	return response


class MyTemplateView(TemplateView):
	
	template_name = "igle/template.html"

	def get_template_names(self):

		if "q" not in self.request.GET:
			return super(MyTemplateView, self).get_template_names()

		return self.request.GET.get("q")

