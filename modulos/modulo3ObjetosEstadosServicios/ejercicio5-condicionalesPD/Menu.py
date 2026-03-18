
''' 
Created on March,2026
@author: lunysska

'''

from Cuenta import *

class Menu:

	# por ahora nuestra clase sólo tiene un atributo.
	def __init__(self, valor, cta):
		self.mensajeDeBienvenida = valor
		self.cuenta = cta

	def darBienvenida(self):
		print(self.mensajeDeBienvenida)

	def despliegaMenu(self):
		print("Las opciones son:")
		print("1. Depositar")
		print("2. Retirar")
		opcion = input("Teclea la opcion:")
		return opcion
		
	def procesaOpcion( self, opcion):
		if(opcion == "1"):
			print("Estas en la opcion de Depositar")
			cantidad = float(input("Ingresa la cantidad a depositar:"))
			if (self.cuenta.depositar(cantidad)):
				print("El deposito se realizo con exito")
		