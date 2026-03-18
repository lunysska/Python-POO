''' 
Created on Feb,2019
@author: lunysska

'''
from Cuenta import *
from Menu import *


class Main:
	pass



#la cantidad de argumentos que se le pasa al constructor, cambia
cuenta1 = Cuenta( 300, "debito" )
cuenta1.imprimirDetalles()
x = 100
print( cuenta1 )

menu = Menu("Bienvenidos al Banco Pato", cuenta1 )
menu.darBienvenida()
opcion = menu.despliegaMenu()
menu.procesaOpcion(opcion)
