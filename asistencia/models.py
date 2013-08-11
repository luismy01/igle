from django.db import models

# Create your models here.

class asistencia(models.Model):
	
	id = models.AutoField(primary_key=True)
	fecha = models.DateField(unique=True)
	hermanos = models.IntegerField()
	visitas = models.IntegerField()
	ninos = models.IntegerField()
	adolescentes = models.IntegerField()
	ofrenda = models.IntegerField()
	observaciones = models.CharField(max_length=250)

	def __unicode__(self):
		return self.fecha

	def dict(self):
		
		obj = {
			"id": self.id,
			"fecha": str(self.fecha),
			"hermanos": self.hermanos,
			"visitas": self.visitas,
			"ninos": self.ninos,
			"adolescentes": self.adolescentes,
			"ofrenda": self.ofrenda,
			"observaciones": self.observaciones
		}

		return obj

	class Meta:
		db_table = "asistencia"
        verbose_name = "asistencia"
        verbose_name_plural = "asistencias"