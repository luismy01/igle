
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from models import Asistencia

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)



class TestAsistencia(TestCase):

	def setUp(self):
		self.asistencia = Asistencia.objects.create(fecha="2014-01-23")

	def test_existe_vista(self):
		print self.client.get("/asistencia/%d" % self.asistencia.id)