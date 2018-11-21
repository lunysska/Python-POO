''' 
Created on November, 2018 
@author: lunysska
'''

from Cuenta import *

class Cliente :

	def __init__( self, n, d, e ) :
		self.nombre = n
		self.direccion = d
		self.edad = e
		self.cuentas = []

	def agregarCuenta( self, cta):
		self.cuentas.append( cta )

	def eliminarCuenta( self, indice ):
		self.cuentas.remove( indice )

	def __str__( self ):
		tmp = "Nombre::" + str( self.nombre )
		tmp += "\nDireccion::" + str( self.direccion )
		tmp += "\nEdad::" + str( self.edad )
		return tmp

	def infoCuentas( self ):
		print ( "---Cantidad de Cuentas:"+ str ( len(self.cuentas)))
		for cta in self.cuentas:
			print ( cta )