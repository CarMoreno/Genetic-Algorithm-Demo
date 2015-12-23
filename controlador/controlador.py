import sys
import re
from vista.vista import *
from modelo.ga import  ga_main
from vista.constantes import PRESENTATION, CONSOLE, GUI, EXIT

class ControladorGenetico(QtGui.QMainWindow):
	"""Recibe los datos de las vistas y valida los campos
	para posteriormente enviar el evento al modelo"""
	def __init__(self, parent=None):
		self.app = QtGui.QApplication(sys.argv)
		QtGui.QWidget.__init__(self, parent)
		self.vista = Ui_MainWindow() #Construimos un objeto vista
		self.vista.setupUi(self)
		self.entrada = self.vista.entrada
		self.button_run = self.vista.run_button
		self.respuesta = self.vista.respuesta
		self.algoritmo_genetico = ga_main
		#Un slot que maneja el evento del botton
		QtCore.QObject.connect(self.button_run, QtCore.SIGNAL('clicked()'), self.run)

	def is_error(self, cadena):
		"""Verifica si en la cadena de entrada hay errores, y retorna un booleano:
		True si encuentra un error, False en caso contrario
		"""
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
		if self.is_error(str(self.entrada.text())):
			self.entrada.setText("Error")
		else:
			print type(self.entrada.text())
			cadena = str(self.entrada.text())
			self.algoritmo_genetico(cadena, self.respuesta, GUI)

	def go(self):
		"""Funcion que se lanza desde el main, desde aca controlamos el flujo de optiones y
		lanzamos la aplicacion de acuerdo a una option"""
		print(PRESENTATION)
		try:
			option = input("What is your choice?: ")
			if option == CONSOLE:	
				while option == CONSOLE:
					target = input("The target: ")
					self.algoritmo_genetico(target, self.respuesta, CONSOLE)
			elif option == GUI:
				while option == GUI:
					self.show()	
					sys.exit(self.app.exec_())
			elif option == EXIT:
				sys.exit()			
			else:
				print("Please, choose only the three options above")
		except Exception, e:
			raise "Please only numbers"
					
