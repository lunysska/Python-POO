# Módulo3. Objetos, Estados, Servicios.

## Relaciones entre objetos

[Ejercicios](ejercicio1-relacionesEntreObjetos/README.txt)

## Flujo de control
### Secuenciales
### Condicionales
### Cíclos

## Publico vs privado
[Ejercicios](ejercicio2-publico-privado/README.txt)

## Objetos como cadenas
[Ejercicios](ejercicio3-objetosComoCadenas/README.txt)

## Tips para mejorar el código fuente
input
**********************
opcion= input('Dame el radio:\n')
print("la opcion::",opcion+8)

*** bapc12

class Cuenta:
    def __init__(self,valor,tipo,propietario):
        self.saldo= valor
        self.tipo= tipo
        self.propietario= propietario
    
    def imprimirDetalles(self):
        print("Desde el metodo")
        print("saldo:",self.saldo)
        print("tipo:",self.tipo)
        print("nombre:",self.propietario)
        
    def depositar(self,deposito):
        if deposito>0:
            print("Depósito exitoso. Su nuevo saldo es de :",self.saldo+deposito)
        else:
            print("Depósito inválido") 
        
    def retirar(self,cantidad):
        if cantidad > self.saldo:
            print("No se puede realizar el retiro.")
        elif self.saldo >= cantidad:
            print("Retiro exitoso. Nuevo saldo:",self.saldo-cantidad)

--------------------------------------------------------------------------------------------------------------------------
https://github.com/victorale1/programaci-nPython/blob/main/teor%C3%ADa/clasesYMetodos/Cuenta.py

''' FECHA: 23 DE FEBRERO DEL 2025
    AUTOR: DE LA MERCED TELLEZ VICTOR ALEJANDRO 
    VERSION:
'''

class Cuenta
  def __init__(self,valor,tipo,nombre)
    self.saldo=valor
    self.tipo=tipo 
    self.nombrePropietario=nombre
  def imprimirDetalles(self)
    print("El estado de su cuenta es:")
    print("Saldo:",self.saldo)
    print("Tipo:",self.tipo)
    print("Nombre:",self.nombrePropietario)
  def retirar(self,cantidad)
    self.saldo=self.saldo-cantidad
    print("usted retiro:",cantidad)
  def depositar(self,cantidad)
    self.saldo=self.saldo+cantidad
    print("Usted deposito:",cantidad)


---------------------------------------------------------------------------------------------------------------------------------
Karlo

La extensión es .Py, debe ser minúscula
#Author: Antonio Karlo Hernandez Pachecano
class Cliente: 
    def __init__(self, nombre, direccion, edad):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
    def imprimirDetalle(self): 
        print("Nombre: ", self.nombre,"Direccion", self.direccion, Edad: ", self.edad)
cliente1= Cliente("Carlos", "calle Epuris 123", 35)
cliente1.imprimirDetalles()

- no va c´odigo de prueba dentro de las clases

#Author: Antonio Karlo Hernandez Pachecano
from Cliente import Cliente
from Cuenta import Cuenta

class Main: 
    pass
class mensajeBienvenida(): 
    def __init__(self):
        pass
    def darBienvenida(self): 
        print("Hola")
        
mensaje = mensajeBienvenida()
mensaje.darBienvenida()

Cliente1 = Cliente("Maria", "Iztapalapa 11", 18)
imprimirDetalles(cliente1)
Cuenta1 = Cuenta(250, "debito", "Maria")

----------------------------------------------------------------------------------------------------------------------------------
Brandon. 

- El readme lleva .txt
----------------------------------------------------------------------------------------------------------------------------------
tiza-develops

def retirar():
    message = input("Indique cuánto desea retirar")
    try:
        persona.saldo = persona.saldo - message
        print("Su nuevo saldo es", persona.saldo)
    except:
        print("Introduzca un número")
        retirar()

******

from Cliente import *
from Cuenta import *

class Main:
    pass

class mensajeBienvenida:
    def __init__():
        pass
    def darBienvenida():
        print("Hola")

mensajeBienvenida.darBienvenida()

Juan = Cliente("Juan","Xochimilco 13", "34")
imprimirDetalles(Juan)

cuenta1 = Cuenta(100,"debito","Juan")

---------------------------------------------------------------------------------------------------------------------------------------


