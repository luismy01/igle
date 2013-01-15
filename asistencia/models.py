from django.db import models

# Create your models here.

class asistencia(models.Model):
	
	fecha = models.DateField(primary_key=True)
	hermanos = models.IntegerField()
	visitas = models.IntegerField()
	ninos = models.IntegerField()

	def __unicode__(self):
		return self.fecha

	class Meta:
		db_table = "asistencia"
        verbose_name = "asistencia"
        verbose_name_plural = "asistencias"