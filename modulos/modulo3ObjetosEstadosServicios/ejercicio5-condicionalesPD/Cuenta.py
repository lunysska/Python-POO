''' 
Created on Febrero,2019 
@author: lunysska

'''
class Cuenta:

	# por ahora nuestra clase sólo tiene un atributo.
	def __init__(self, valor, tipo):
		self.cantidad = valor
		self.tipo = tipo

	#informacion
	def imprimirDetalles(self):
		print(self.cantidad)
		print(self.tipo)

	def retirar(self, cantidad):
		self.cantidad = self.cantidad - cantidad 

	def depositar(self, cantidad):
		if cantidad > 0 :
			self.cantidad = self.cantidad + cantidad
			return True 
		else:
			return False

	def __str__(self):
		return "Saldo::" + str(self.cantidad) + "::Tipo::" + self.tipo




