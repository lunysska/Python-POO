''' 
Created on September, 2018 
@author: lunysska

''' 

from Cuenta import *

class CuentaHija(Cuenta):

	def __init__( self, valor, tipo ):
		Cuenta.__init__(self, valor)
		self.__tipo = tipo
