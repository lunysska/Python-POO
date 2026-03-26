''' 
Created on November, 2018 
@author: lunysska

''' 
Esta versión incluye el uso de herencia para la clase Cuenta.

- Algo importante a notar es que los atributos de la clase Madre
se han tenido que cambiar de acceso para moder accederlos desde la clase Hija

- En el caso de la clase CuentaDeAhorro no se ha implementado la parte
de los intereses al mes, dado que no estamos en condiciones de hacerlo, aún.

- En el caso de la clase CuentaDeCredito se tuvo que sobreescribir el método "retirar" para que se adecue a la especificación, en este se envía un mensaje a la consola cuando no se logra hacer el retiro, mismo que no debería ir, en un sentido estricto de diseño, pues se regresa un valor booleano, sin embargo en esta versión se realizó, para resaltar este caso.



