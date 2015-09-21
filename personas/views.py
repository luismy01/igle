from django.core.urlresolvers import reverse_lazy
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.views.generic import CreateView, DetailView, ListView, TemplateView, UpdateView, View
from django.views.generic.list import MultipleObjectMixin
from .forms import PersonaForm
from .models import Persona
from .mixins import JSONResponseMixin
import json


class PersonaListView(JSONResponseMixin, ListView):
	
	context_object_name = "personas"
	model = Persona
	paginate_by = 2
	template_name = "personas/list.html"


	def delete(self, request, *args, **kwargs):

		id_persona = kwargs["id"]

		p = Persona.objects.get(id=id_persona)
		p.delete()

		return JsonResponse(data={"result": "ok"}, safe=False)
		

	def get_context_data(self, **kwargs):

		context_data = super(PersonaListView, self).get_context_data(**kwargs)
		object_list = context_data["object_list"]

		queryset = [ model_to_dict(item) for item in object_list ]
		
		for item in queryset:
			item["fecha_nacimiento"] = str(item["fecha_nacimiento"])

		json_data = json.dumps(queryset)

		
		context_data["json_data"] = json_data

		return context_data



	def post(self, request, *args, **kwargs):

		json_data = None
		CONTENT_TYPE = str(request.META["CONTENT_TYPE"])

		# content-type: application/json
		if "application/json" in CONTENT_TYPE:
			json_data = json.loads(request.read())

		# content-type: application/x-www-form-urlencoded
		if "model" in request.POST:

			json_data = json.loads(request.POST["model"])

		p = Persona()
		
		p.nombre = json_data["nombre"]
		p.email = json_data["email"]
		p.celular = json_data["celular"]
		p.fecha_nacimiento = json_data["fecha_nacimiento"]
		p.habilitado = json_data["habilitado"]
		p.genero = json_data["genero"]
		p.identificacion_tipo = json_data["identificacion_tipo"]
		p.identificacion_codigo = json_data["identificacion_codigo"]
		p.congregacion = json_data["congregacion"]
		
		p.save()
		json_data["id"] = p.id

		return JsonResponse(data=json_data, safe=False)


	def render_to_response(self, context):

		if self.request.GET.get('format') == 'json':
			return self.render_to_json_response(context, safe=False)
		else:
			return super(PersonaListView, self).render_to_response(context)


	def get_data(self, context):

		if "json_data" in context:
			return context["json_data"]
		else:
			return None


class PersonaEditView(UpdateView):

	fields = ['nombre', 'identificacion_codigo', 'congregacion', 'fecha_nacimiento', 'email', 'celular', 'genero']
	model = Persona
	queryset = Persona.objects.all()
	template_name = "personas/persona_edit_form.html"
	slug_field = "identificacion_codigo"

	def get(self, request, *args, **kwargs):

		print model_to_dict(self.get_object())

		return super(PersonaEditView, self).get(request, *args, **kwargs)


class PersonaDetailView(DetailView):

	context_object_name = "persona"
	queryset = Persona.objects.all()
	template_name = "personas/persona_view_form.html"
	slug_field = "identificacion_codigo"

	def get(self, request, *args, **kwargs):

		print model_to_dict(self.get_object())

		return super(PersonaDetailView, self).get(request, *args, **kwargs)



class PersonaCreateView(CreateView):

	form_class = PersonaForm
	template_name = "personas/persona_create_form.html"
	success_url = reverse_lazy('personas:list_view')

	def get(self, request, *args, **kwargs):
		print "PersonaCreateView: get method"
		return super(PersonaCreateView, self).get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		print "PersonaCreateView: post method"
		return super(PersonaCreateView, self).post(request, *args, **kwargs)
