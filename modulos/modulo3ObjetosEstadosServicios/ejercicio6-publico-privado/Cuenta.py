''' 
Created on September, 2018 
@author: lunysska

''' 
class Cuenta:

	def __init__(self, valor):
		"""volvemos privado el atributo cantidad para que no pueda
			ser accedido desde otras clases"""
		self.__cantidad = valor

	def depositar(self, valor):
		if valor > 0:
			self.__cantidad = self.__cantidad + valor
		else:
			print ("El valor para depositar es erroneo")

	def mostrarDetalles(self):
		print ("La cantidad de la cuenta::", self.__cantidad)