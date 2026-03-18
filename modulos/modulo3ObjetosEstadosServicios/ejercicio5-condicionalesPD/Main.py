''' 
Created on Feb,2019
@author: lunysska

'''
from Cuenta import *
from Menu import *

class Main:
	pass


menu = Menu("Bienvenidos al Banco Pato")
menu.darBienvenida()
opcion = menu.despliegaMenu()
menu.procesaOpcion(opcion)
