''' 
Created on November, 2018 
@author: lunysska

''' 

from Cuenta import *
from CuentaAhorro import *
from CuentaCredito import *
from Cliente import *

class Pruebas:
	pass

	print ( "\t *********Un objeto Cuenta" )
	cuenta1 = Cuenta( 300 )
	print (cuenta1)
	cuenta1.depositar( 400 )
	print (cuenta1)

	print ( "\n\n\t *********La Cuenta de Ahorro" )
	cuenta2 = CuentaAhorro( 200, 0.2 )
	print (cuenta2) 
	cuenta2.depositar( 8000 )
	print (cuenta2)

	print ( "\n\n\t *********La cuenta de Credito" )
	cuenta3 = CuentaCredito( 200, 100 )
	print (cuenta3) 
	cuenta3.depositar( 8000 )
	print (cuenta3)
	cuenta3.retirar(8250)
	print (cuenta3)
	cuenta3.retirar(150)
	print (cuenta3)

	print ( "\n\n\t *********Objeto Cliente:sin cuentas" )
	cliente1 = Cliente( "Alejandro", "Calle Flores No.25", 56 )
	print ( str(cliente1))
	cliente1.infoCuentas()

	print ( "\t\t .... agregando cuentas" )
	cliente1.agregarCuenta( cuenta1 )
	cliente1.agregarCuenta( cuenta2 )
	cliente1.agregarCuenta( cuenta3 )
	cliente1.infoCuentas()
	print ( "\n\t\t .... borrando cuentas" )
	cliente1.eliminarCuenta( cuenta1 )
	cliente1.infoCuentas()
