
from django.conf.urls import patterns, url
from django.views.generic.simple import direct_to_template
from secretary.views import buscar_miembros, listar_miembros

urlpatterns = patterns('',
    url(r'^list-members$',  listar_miembros, name="listar_miembros"),
    url(r'^search-members$', buscar_miembros, name = "buscar"),
)

