''' 
Created on September, 2018 
@author: lunysska

''' 

from Cuenta import *
from Cliente import *

class Main:
	pass
print ( "Desde las pruebas" )
cuenta1 = Cuenta( 300 )
print ( cuenta1 )
cuenta1.depositar( 400 )
print ( cuenta1 )

"""
Imprimimos un objeto y nos mandará una referencia en la memoria
si es que no tenemos reescrito el me´todo __str__
"""
print ("Objeto cuenta::", cuenta1)

cliente = Cliente( "Virginia", "direccion", 25, cuenta1)
print ("Objeto cliente::", cliente )
