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

**__str__**: Este método se utiliza para definir la representación en cadena de un objeto que sea legible para humanos. Es llamado por la función integrada **str()** y por la función **print**.<br>

``` python
class Car:
    def __str__(self):
        return f"{self.make} {self.model}"
```

[Ejercicios](ejercicio3-objetosComoCadenas/README.txt)

