''' 
Created on September, 2018 
@author: lunysska

''' 

from Cuenta import *
from CuentaHija import *
from Cliente import *

class Pruebas:
	pass

	print ( "\t *********La clase madre" )
	cuenta1 = Cuenta( 300 )
	print (cuenta1)
	cuenta1.depositar( 400 )
	print (cuenta1)

	print ( "\n\n\t *********La clase hija" )
	cuenta2 = CuentaHija( 200, "debito" )
	print (cuenta2) 
	cuenta2.depositar( 8000 )
	print (cuenta2)

	print ( "\n\n\t *********La clase Cliente" )

	cliente = Cliente( "Virginia", "direccion", 25, cuenta1)
	print ("Objeto cliente::", cliente )
