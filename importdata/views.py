

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from gspread import login

from asistencia.models import Asistencia

SpreadSheetkey = '0AnFzMPX5K-trdHNpNFY2aXE0OTVEY0pTUU9faUJ2OEE'
email = "luismy01@gmail.com"
password = "cristo.te.ama"

def get_asistencia(fecha):
	try:
		return Asistencia.objects.get(fecha=fecha)
	except Asistencia.DoesNotExist:
		return Asistencia()

def import_view(request):

	client = login(email, password)
	spread = client.open_by_key(key=SpreadSheetkey)
	worksheet = spread.get_worksheet(0)
	records = worksheet.get_all_records()

	n = len(records)
	m = 0
	for row in records:
		try:
			a = get_asistencia(row['FECHA'])
			a.fecha = row['FECHA']
			a.hermanos = int(row['HERMANOS'])
			a.visitas = int(row['VISITAS'])
			a.ninos = int(row['NINOS'])
			a.adolescentes = int(row['ADOLESCENTES'])
			a.ofrenda = int(row['OFRENDA'])
			a.observaciones = row['OBSERVACIONES']
			
			a.save()
			failed = False
			m += 1

		except:
			failed = True

		sms = "%s: %s" % (a.fecha, "SI" if not failed else "NO")
		#messages.add_message(request, messages.INFO, sms)
		print sms
	
	sms = "Se importaron %d de %d asistencias." % (m, n)
	messages.add_message(request, messages.INFO, sms)
	return redirect('/')
	