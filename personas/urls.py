from django.conf.urls import patterns, url
from django.views.generic import TemplateView

template = "personas/persona_template.html"

urlpatterns = patterns('',
    url(r'^$',  TemplateView.as_view(template_name = template), name="personas_view"),
)