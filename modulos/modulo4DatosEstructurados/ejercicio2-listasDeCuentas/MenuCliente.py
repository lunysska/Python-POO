''' 
Created on November, 2018 
@update: March, 2026
@author: lunysska

''' 

from Cuenta import *
from Cliente import *

class MenuCliente:

	def __init__( self ) :
		self.__bienvenida = "Menu del Usuario"
		self.__cliente = Cliente("Marco","Calle de Arboledas No. 45, Col. Granjas México. CDMX",38)

	def menuCuentas( self ):
		opciones = "*********** \n Menu Cuenta \n ***********\n"
		opciones += "Este es nuestro menu::\n"
		opciones += "1. Agregar una Cuenta\n"
		opciones += "2. Eliminar una Cuenta\n"
		opciones += "\n"

		print( opciones )
		opcion = input("Teclee la opcion deseada::")
		print("Elegiste:"+opcion)
		if opcion == "1":
			self.__agregarCuenta()
		elif opcion == "2":
			print("Se está construyendo esa opcion")
		else: 
			print ("Esa opción no existe")

	# por qué este método es privado.
	def __agregarCuenta( self ):
		despliega = "Eligió la opción:: Agregar una Cuenta\n"
		print ( "Inserte los siguientes datos:\n")
		saldoInicial = float(input("\t\t El saldo inicial::"))
		cuenta = Cuenta(saldoInicial)
		self.__cliente.agregarCuenta(cuenta)
		print("La cuenta se agregó con éxito")
		self.__cliente.infoCuentas()

						
		