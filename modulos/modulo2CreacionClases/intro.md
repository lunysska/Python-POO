# Creacion de clases
## qué son las clases, 
- significado,
- diseño
- sintáxis
### los atributos
- en sintáxis
- significado
  
[Ejercicios](ejercicio1-operadorPunto/README.md)

### los métodos, 
- lo que son,
- las ventajas de tener métodos,
- como se definen en diseño,
- en sintáxis
 
[Ejercicios](ejercicio2-metodosVSMain/ejercicio2-metodosVSMain.md)

## Datos en Python

### cadenas de texto
### enteros, flotantes y booleanos

## Convenciones de nombrado en Python
Las convenciones de nombrado de variables son muy importantes porque nos dan limpieza en el código y un mayor entendimiento del mismo, incluso antes de ir a leer la documentación. Por tal motivo se considera un principio de programación.

En Python y en esta clase usaremos:

- sustantivo para nombres de variables y atributos, empezando con minúscula.
  ``` python
    int edad
    int edadRegistro
    int edad_registro
  ```
- sustantivo para nombres de clases, empezando con Mayúscula
  ``` python
    class Estudiante
    class EstudianteUniversitario
    class Estudiante_Universitario
    EstudianteUniversitario estudiante = EstudianteUniversitario("Adolfo", 35)
  ```
  
- verbos para nombres de métodos, empezando con minúscula
  ``` python
    validar()
    validarNombre()
    validar_nombre()
  ```

- nombres de proyectos y paquetes son sustantivos, empezando en minúscula y no llevan espacios
  ``` python
    sistemaInventario
    sistema
  ```  

[Acá se puede leer con más detenimiento](https://peps-python-org.translate.goog/pep-0008/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc)



## Operaciones de Entrada/Salida en Consola

```python:
nombre = input("Ingrese su nombre: ")
print(nombre)
nombre = input("Ingrese su nombre: ")
```

## Tips de mejoras en código

En cada capítulo tenemos algunas sugerencias de mejoras de códigos que hemos visto que se realizan en el código de manera continua

- Código 1
```python:
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
```
- Código 2
```python:
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
```

- Código 3
```python:
Nombre de Archivo: Cliente.Py
class Cliente: 
    def __init__(self, nombre, direccion, edad):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
    def imprimirDetalle(self): 
        print("Nombre: ", self.nombre,"Direccion", self.direccion, Edad: ", self.edad)
cliente1= Cliente("Carlos", "calle Epuris 123", 35)
cliente1.imprimirDetalles()
```

- Código 4
```python:
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
```

- Código 5
```python:
#Acá incluye archivo que se llama "readme"

def retirar():
    message = input("Indique cuánto desea retirar")
    try:
        persona.saldo = persona.saldo - message
        print("Su nuevo saldo es", persona.saldo)
    except:
        print("Introduzca un número")
        retirar()

######
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
```
