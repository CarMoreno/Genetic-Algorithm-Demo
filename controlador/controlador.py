import sys
import re
from vista.vista import *
from modelo.ga import  ga_main

class ControladorGenetico(QtGui.QMainWindow):
	"""Recibe los datos de las vistas y valida los campos
	para posteriormente enviar el evento al modelo"""
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.vista = Ui_MainWindow() #Construimos un objeto vista
		self.vista.setupUi(self)
		self.entrada = self.vista.entrada
		self.button_run = self.vista.run_button
		self.respuesta = self.vista.respuesta
		self.algoritmo_genetico = ga_main
		#Un slot que maneja el evento del botton
		QtCore.QObject.connect(self.button_run, QtCore.SIGNAL('clicked()'), self.run)

	def is_error(self):
		"""Verifica si en la cadena de entrada hay errores, y retorna un booleano:
		True si encuntra un error, False en caso contrario
		"""
		cadena = str(self.entrada.text())
		if cadena.isalpha():
			return True
		elif "/" in cadena or '*' in cadena or '+' in cadena or '-' in cadena:
			return True
		elif cadena.count('.') > 1:
			return True	 	
		else:
			return False		
		
	def run(self):
		"""Funcion que se lanza cuando se da click en el boton 'Run', presente en la vista"""
		if self.is_error():
			self.entrada.setText("Error")
		else:
			print type(self.entrada.text())
			cadena = str(self.entrada.text())
			self.algoritmo_genetico(cadena, self.respuesta)
		