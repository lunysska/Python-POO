# Herencia en el Sistema del Banco

La herencia al ser un concepto dentro de los primordiales en este paradigma de POO se puede aplicar en muchos aspectos dentro de un sistema grande como lo es el Sistema del Banco.

En este caso lo vamos a usar en definir los tipos de cuentas dentro del Banco. Generaremos una clase madre de Cuenta General, en donde se describan los atributos generales que toda cuenta debe tener y posteriormente haremos clases hijas que se especialicen en agregar nuevos atributos y sobreescribir los métodos.

## Ejemplo 1.

Este ejemplo muestra el uso de herencia en Python, con dos clases muy simples (semánticamente no tienen mucho sentido)

En este caso sólo se muestra:
a) La síntáxis para herencia (en "CuentaHija")
b) La herencia de métodos de una clase madre (Cuenta) a una hija (CuentaHija)
	con el método "depositar"
c) Que al heredar hay me´todos que el algoritmo de la madre no es "suficiente" para la hija
	con el método "__str__"

## Ejemplo 2.

### Versión 1
Este ejemplo muestra el uso de sobreescritura de métodos en Python, con dos clases muy simples (semánticamente no tienen mucho sentido), es sòlo para empezar a introducir el primer concepto de herencia en el sistema

*** ver 1: Algo importante de este ejercicio es que usa "mensajes" para resaltar la procedencia de las invocaciones

En este caso sólo se muestra:
a) Que la clase Hija (CuentaHija) sobreescribe el método "__str__", pero lo hace reusando la escritura del método "__str__" de la madre

### Versiòn 2
''' 
Este ejemplo muestra el uso de sobreescritura de métodos en Python, con dos clases muy simples (semánticamente no tienen mucho sentido)
***ver 2. Se eliminan los mensajes que servían para resaltar.
En este caso sólo se muestra:
a) Que la clase Hija (CuentaHija) sobreescribe el método "__str__", pero lo hace reusando la escritura del método "__str__" de la madre

## Ejemplo 3.

Esta versión incluye el uso de herencia para la clase Cuenta.

- Algo importante a notar es que los atributos de la clase Madre
se han tenido que cambiar de acceso para moder accederlos desde la clase Hija

- En el caso de la clase CuentaDeAhorro no se ha implementado la parte
de los intereses al mes, dado que no estamos en condiciones de hacerlo, aún.

- En el caso de la clase CuentaDeCredito se tuvo que sobreescribir el método "retirar" para que se adecue a la especificación, en este se envía un mensaje a la consola cuando no se logra hacer el retiro, mismo que no debería ir, en un sentido estricto de diseño, pues se regresa un valor booleano, sin embargo en esta versión se realizó, para resaltar este caso.
