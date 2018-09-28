''' 
Created on September, 2018 
@author: lunysska

''' 

from Cuenta import *
from Cliente import *

class Pruebas:
	pass
print ("Desde las pruebas")
cuenta1 = Cuenta( 300 )
cuenta1.mostrarDetalles()
cuenta1.depositar( 400 )
cuenta1.mostrarDetalles()

"""
	Este print esta enviando a la salida estandar un objeto
	Que imprime
"""
print ("va::", cuenta1)

"""
Si el atributo cantidad fuera publico, entonces
se puede acceder desde cualquier lado, originando "errores semanticos"
"""
print ("Intentamos imprimir un atributo privado")
print ("El valor de la cuenta es::", cuenta1.__cantidad)

cuenta1.mostrarDetalles()
cliente = Cliente( "Virginia", "direccion", 25, cuenta1)
cliente.mostrarDetalles()