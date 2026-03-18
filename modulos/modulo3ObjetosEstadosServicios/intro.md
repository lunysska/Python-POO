# Módulo3. Objetos, Estados, Servicios.

## Relaciones entre objetos
Existen diferentes tipos de relaciones entre clases. En esta sección sólo consideraremos La relación "tiene una" (o
has-a en inglés) en Python se implementa mediante la composición o agregación, donde una clase contiene una instancia de otra clase como atributo.

### Puntos clave:
- **Implementación:** Se define una clase y, dentro de su método __init__, se crea o recibe una instancia de otra clase.
- **Uso:** Permite que objetos complejos se construyan reutilizando componentes más pequeños y especializados.
- **Ventajas:** Mayor flexibilidad y modularidad en el diseño

´´´ python
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

class Carro:
    def __init__(self, marca, tipo_motor):
        self.marca = marca
        # Aquí se crea la relación "tiene una"
        self.motor = Motor(tipo_motor) 

# Uso
mi_carro = Carro("Toyota", "V6")
print(f"{mi_carro.marca} tiene un motor {mi_carro.motor.tipo}")

´´´

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

