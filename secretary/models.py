
from django.db import models

# Create your models here.

TIPOS_IDENTIF = (
    ('TI', 'Tarjeta de Identidad'),
    ('CC', 'Cedula de Ciudadania'),
    ('CE', 'Cedula de Extranjeria'),
    ('PS', 'Pasaporte'),
)

GENEROS = (
    ('M', 'Masculino'),
    ('F', 'Femenino'),
)

ESTADO_CIVIL = (
    ('SL', 'Soltero'),
    ('CP', 'Comprometido'),
    ('CS', 'Casado'),
    ('VD', 'Viudo'),
    ('DV', 'Divorciado'),
    
)

class Miembro(models.Model):
    
    identificacion = models.CharField(max_length=15, primary_key=True)
    tipoIdentif = models.CharField(max_length=3, choices=TIPOS_IDENTIF)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=20)
    ocupacion = models.CharField(max_length=15)
    genero = models.CharField(max_length=1, choices=GENEROS)
    estadoCivil = models.CharField(max_length=2, choices=ESTADO_CIVIL)
    folio = models.CharField(max_length=3)
    
    telefono = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    email = models.EmailField()
    
    fechaNac = models.DateField()
    lugarNac = models.CharField(max_length=20)
    
    barrio = models.CharField(max_length=20)
    direccion = models.CharField(max_length=30)
    
    nompadre = models.CharField(max_length=30)
    nommadre = models.CharField(max_length=30)
    nomconyuge = models.CharField(max_length=30)
    
    fechaBautismo = models.DateField(null=True)
    lugarBautismo = models.CharField(max_length=30)
    pastorBautismo = models.CharField(max_length=30)
    fechaEspirituSanto = models.DateField(null=True)
    
    bautizado = models.BooleanField()
    trasladado = models.BooleanField()
    apartado = models.BooleanField()
    
    observaciones = models.CharField(max_length=160)
    