# Módulo 6. Manejo de Errores

## 6.1 Excepciones
Una expresión es sintácticamente correcta, puede generar un error cuando se intenta ejecutar. Los errores detectados durante la ejecución se llaman 
excepciones, y no son incondicionalmente fatales: pronto aprenderás a gestionarlos en programas Python. Sin embargo, la mayoría de las excepciones no 
son gestionadas por el código, y resultan en mensajes de error como los mostrados aquí:

``` python
10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    10 * (1/0)
          ~^~
ZeroDivisionError: division by zero
4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    4 + spam*3
        ^^^^
NameError: name 'spam' is not defined
'2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    '2' + 2
    ~~~~^~~
TypeError: can only concatenate str (not "int") to str
```

## 6.2. Gestionando excepciones
Es posible escribir programas que gestionen determinadas excepciones. Véase el siguiente ejemplo, que le pide al usuario una entrada hasta que ingrese 
un entero válido, pero permite al usuario interrumpir el programa (usando Control-C o lo que soporte el sistema operativo); nótese que una interrupción
generada por el usuario es señalizada generando la excepción **KeyboardInterrupt**.

``` python
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
```
La sentencia try funciona de la siguiente manera:

    - Primero, se ejecuta la cláusula try (la(s) linea(s) entre las palabras reservadas try y la except).
    - Si no ocurre ninguna excepción, la cláusula except se omite y la ejecución de la cláusula try finaliza.
    - Si ocurre una excepción durante la ejecución de la cláusula try, se omite el resto de la cláusula. Luego, si su tipo coincide con la excepción 
    nombrada después de la palabra clave except, se ejecuta la cláusula except, y luego la ejecución continúa después del bloque try/except.

## 6.3 Manejo de errores en el sistema del Banco
Cómo pruebo todos estos conceptos en el sistema del Banco.?
En este ejercicio se contempla el uso para manejo de fechas, el código que se muestra es una forma sencilla de validar la construcción de fechas.
El estudiante decidirá en qué clase puede incluir este tipo de validaciones (hay varios lugares donde se pueden usar.)
[Tipo Fecha](README.md)

## 6.4 Referencias

- https://docs.python.org/es/3/tutorial/errors.html
- https://ellibrodepython.com/excepciones-try-except-finally   


