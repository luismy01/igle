from django.db import models
from django.contrib.auth.models import User

class Asistencia(models.Model):
	id = models.AutoField(primary_key=True)
	fecha = models.DateField(unique=True)
	hermanos = models.PositiveIntegerField()
	visitas = models.PositiveIntegerField()
	ninos = models.PositiveIntegerField()
	adolescentes = models.PositiveIntegerField()
	ofrenda = models.PositiveIntegerField()
	observaciones = models.CharField(max_length=250)
	#user = models.ForeignKey(User)

	# Indica el total de la asistencia
	def total(self):
		return self.hermanos + self.visitas + self.ninos + self.adolescentes
 
	def __unicode__(self):
		#return self.fecha.strftime("%Y-%m-%d")
		return self.fecha.format("%Y-%m-%d")

	def dict(self):
		
		obj = {
			"id": self.id,
			"fecha": str(self.fecha),
			"hermanos": self.hermanos,
			"visitas": self.visitas,
			"ninos": self.ninos,
			"adolescentes": self.adolescentes,
			"ofrenda": self.ofrenda,
			"observaciones": str(self.observaciones)
		}

		return obj

	class Meta:
		db_table = "asistencia"
        verbose_name = "asistencia"
        verbose_name_plural = "asistencias"

