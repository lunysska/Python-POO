''' 
Created on November, 2018 
@author: lunysska

''' 

from Cuenta import *
from CuentaAhorro import *
from CuentaCredito import *

class MenuUsuario:

	def __init__( self ) :
		self.bienvenida = "Menu del Usuario"

	def menuCuenta( self ):
		opciones = "Menu Cuenta"
		opciones += "Teclee la opcion que desee"
		opciones += "1. Agregar una Cuenta"

		print( opciones )
		opcion = input()
		print("Elegiste:"+opcion)

		if opcion == "1":
			self.agregarCuenta()
		else:
			print ("Eligió la opción NO correcta")

	def agregarCuenta( self ):
		despliega = "Eligió la opción:: Agregar una Cuenta\n"
		despliega += "\t Tipos de Cuenta \n"
		despliega += "\t 1. Cuenta de Ahorro\n"
		despliega += "\t 2. Cuenta de Credito\n"
		despliega += "\t Elija el tipo de cuenta que desea agregar\n"

		print( despliega )
		opcion = input()
		if opcion == "1":
			print ( "Eligió la opción:: Agregar una Cuenta" )
		else:
			print ( "Eligió la opción NO correcta" )
