''' 
Created on November, 2018 
@author: lunysska

''' 

from Cuenta import *
from Cliente import *
from CuentaAhorro import *
from CuentaCredito import *

class MenuUsuario:

	def __init__( self ) :
		self.bienvenida = "Menu del Usuario"


	def menuCuenta( self ):

		#Aca genero un cliente, pero bien podría ser por un metodo
		# o como atributo de la clase
		cte = Cliente ("Virginia", "direccion de Virginia", 32 )

		opciones = "Menu Cuenta"
		opciones += "Teclee la opcion que desee"
		opciones += "1. Agregar una Cuenta"
		opciones += "2. Eliminar una Cuenta"

		print( opciones )
		opcion = input()
		print("Elegiste:"+opcion)

		if opcion == "1":
			self.agregarCuenta( cte )
		else:
			print ("Eligió la opción NO correcta")


	def agregarCuenta( self, cte ):
		despliega = "Eligió la opción:: Agregar una Cuenta \n"
		despliega += "\t Tipos de Cuenta \n"
		despliega += "\t 1. Cuenta de Ahorro \n"
		despliega += "\t 2. Cuenta de Credito \n"
		despliega += "\t Elija el tipo de cuenta que desea agregar \n"

		print( despliega )
		opcion = input()

		if opcion == "1":
			print ( "Eligió la opción:: Agregar una Cuenta de Ahorro" )
			#se tiene que generar la cuenta de ahorro, en iteracción con
			#el cliente.
			#en este ejemplo la cuenta está fija
			#si queda muy largo el código, tal vez convenga otro metodo
			cta = CuentaAhorro( 2000, 0.8 )
			cte.agregarCuenta(cta) 
		else:
			print ( "Eligió la opción NO correcta" )

	