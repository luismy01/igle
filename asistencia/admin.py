
from django.contrib import admin
from asistencia.models import Asistencia

ASISTENCIA_REFERENCIA = 100

class AsistenciaAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'hermanos', 'visitas', 'ninos', 'adolescentes', 'ofrenda', 'total', 'avatar','esAlta','esBaja')
	list_filter = ('fecha',)
	list_editable = ('ofrenda',)
	search_fields = ('hermanos', 'observaciones')
	#actions = (export_as_xls, )

	# Indica si la asistencia es alta, segun la ASISTENCIA_REFERENCIA
	def esAlta(self, obj):
		return obj.total() >= ASISTENCIA_REFERENCIA

	# le dice al admin de django que la funcion retorna un dato booleano
	esAlta.boolean = True

	# Indica si la asistencia es baja, segun la ASISTENCIA_REFERENCIA
	def esBaja(self, obj):
		return obj.total() < ASISTENCIA_REFERENCIA

	# le dice al admin de django que la funcion retorna un dato booleano
	esBaja.boolean = True

	def avatar(self, obj):
		return """
			<img src="http://www.artifacting.com/blog/wp-content/uploads/2010/11/Baseball_hat.jpg"></img>
		"""
	# Esto le dice a django que el codigo retornado por la funcion, lo puede renderizar de forma segura
	avatar.allow_tags = True

	# Esto asocia la funcion a un campo del modelo para efectos de ordamiento en el admin de django
	avatar.admin_order_field = 'hermanos'

admin.site.register(Asistencia, AsistenciaAdmin)
