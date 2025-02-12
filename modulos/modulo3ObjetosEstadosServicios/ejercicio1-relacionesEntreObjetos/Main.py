''' 
Created on August,2018 
@author: lunysska

'''
from Cuenta import *
from Cliente import *

class Main:
	pass
print ("Desde las pruebas")
cuenta1 = Cuenta( 300 )
cuenta1.mostrarDetalles()
cuenta1.depositar( 400 )
cuenta1.mostrarDetalles()

cliente = Cliente( "Virginia", "direccion", 25, cuenta1)
cliente.mostrarDetalles()