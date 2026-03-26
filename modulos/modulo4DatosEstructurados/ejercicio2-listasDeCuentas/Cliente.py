''' 
Created on November, 2018 
@author: lunysska
@update: March, 2026
'''

from Cuenta import *

class Cliente :

	def __init__( self, n, d, e ) :
		self.__nombre = n
		self.__direccion = d
		self.__edad = e
		self.__cuentas = [] # empezamos con una lista vacia

	def agregarCuenta( self, cta):
		self.__cuentas.append( cta )

	def eliminarCuenta( self, indice ):
		self.__cuentas.remove( indice )

	def __str__( self ):
		tmp = "Nombre::" + str( self.__nombre )
		tmp += "\nDireccion::" + str( self.__direccion )
		tmp += "\nEdad::" + str( self.__edad )
		return tmp

	def infoCuentas( self ):
		print ( "---Cantidad de Cuentas:"+ str(len(self.__cuentas)))
		for cta in self.__cuentas:
			print ( cta )