''' 
Created on November, 2018 
@author: lunysska
''' 

class Cuenta:

	def __init__( self, valor ):
		self.cantidad = valor

	def depositar( self, valor ):
		if valor > 0:
			self.cantidad = self.cantidad + valor
			return True
		else:
			return False

	def retirar( self, valor ):
		if valor > 0:
			self.cantidad = self.cantidad - valor
			return True
		else:
			return False

	def __str__( self ):
		return "::La cantidad de la cuenta::" + str( self.cantidad )