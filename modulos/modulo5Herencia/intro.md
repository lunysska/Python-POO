#Herencia

La programación orientada a objetos nos permite crear clases que pueden heredar propiedades, métodos y comportamientos de otras clases ya existentes. En Python, la herencia es una característica clave que nos permite crear clases hijas a partir de una clase padre.

La herencia en Python se logra por medio de una sintáxis sencilla que involucra la creación de una nueva clase que hereda atributos y métodos de la clase padre. Para crear una clase hija en Python, simplemente agregamos el nombre de la clase padre en paréntesis después del nombre de la clase hija.

``` python
# Clase Padre
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        pass

# Clase Hija
class Perro(Animal):
    def hablar(self):
        return "¡Guau!"

# Uso
mi_perro = Perro("Fido")
```
```print(mi_perro.nombre)  # Heredado: Fido
print(mi_perro.hablar()) # Sobrescrito: ¡Guau!
