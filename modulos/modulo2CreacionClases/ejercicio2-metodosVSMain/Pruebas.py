''' 
Created on Feb,2019
@author: lunysska

'''
from Cuenta import *

class Pruebas:
	pass

print ("*** 1. Imprimimos atributos desde el archivo principal")

#la cantidad de argumentos que se le pasa al constructor, cambia
cuenta1 = Cuenta( 300, "debito" )

#si fueran muchos atributos, acá aparecerían muchisimas 
#lineas
print (cuenta1.cantidad)
print (cuenta1.tipo)

print ("\n\n*** 2. Imprimimos atributos con el método")
cuenta1.imprimirDetalles()

