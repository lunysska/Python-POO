# 5. Herencia

La programación orientada a objetos nos permite crear clases que pueden heredar propiedades, métodos y comportamientos de otras clases ya existentes. En Python, la herencia es una característica clave que nos permite crear clases hijas a partir de una clase madre.

La herencia en Python se logra por medio de una sintáxis sencilla que involucra la creación de una nueva clase que hereda atributos y métodos de la clase madre. Para crear una clase hija en Python, simplemente agregamos el nombre de la clase padre en paréntesis después del nombre de la clase hija.

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

## 5.1. Ventajas de la herencia
Dado que una clase hija hereda los atributos y métodos de la padre, nos puede ser muy útil cuando tengamos clases que se parecen entre sí pero tienen ciertas particularidades. En este caso en vez de definir un montón de clases para cada animal, podemos tomar los elementos comunes y crear una clase Animal de la que hereden el resto, respetando por tanto la filosofía **DRY**. Realizar estas abstracciones y buscar el denominador común para definir una clase de la que hereden las demás, es una tarea de lo más compleja en el mundo de la programación.

Para saber más: El principio DRY (Don't Repeat Yourself) es muy aplicado en el mundo de la programación y consiste en no repetir código de manera innecesaria. Cuanto más código duplicado exista, más difícil será de modificar y más fácil será crear inconsistencias. Las clases y la herencia a no repetir código.

## 5.2. Extendiendo y modificando métodos

Continuemos con nuestro ejemplo de perros y animales. Vamos a definir una clase padre Animal que tendrá todos los atributos y métodos genéricos que los animales pueden tener. Esta tarea de buscar el denominador común es muy importante en programación. Veamos los atributos:

    - Tenemos la especie ya que todos los animales pertenecen a una.
    - Y la edad, ya que todo ser vivo nace, crece, se reproduce y muere.

Y los métodos o funcionalidades:

    - Tendremos el método hablar, que cada animal implementará de una forma. Los perros ladran, las abejas zumban y los caballos relinchan.
    - Un método moverse. Unos animales lo harán caminando, otros volando.
    - Y por último un método descríbeme que será común.

Definimos la clase padre, con una serie de atributos comunes para todos los animales como hemos indicado.

``` python
class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    # Método genérico pero con implementación particular
    def hablar(self):
        # Método vacío
        pass

    # Método genérico pero con implementación particular
    def moverse(self):
        # Método vacío
        pass

    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)
```

Tenemos ya por lo tanto una clase genérica Animal, que generaliza las características y funcionalidades que todo animal puede tener. Ahora creamos una clase Perro que hereda del Animal. Como primer ejemplo vamos a crear una clase vacía, para ver como los métodos y atributos son heredados por defecto.

``` python
# Perro hereda de Animal
class Perro(Animal):
    pass

mi_perro = Perro('mamífero', 10)
mi_perro.describeme()
# Soy un Animal del tipo Perro
```

Con tan solo un par de líneas de código, hemos creado una clase nueva que tiene todo el contenido que la clase padre tiene, pero aquí viene lo que es de verdad interesante, de manera análoga, se pueden crear varios animales concretos y sobreescrbir algunos de los métodos que habían sido definidos en la clase Animal, como el hablar o el moverse, ya que cada animal se comporta de una manera distinta.

## 5.3 Conceptos Clave de la Herencia

    - Reutilización de Código: Evita reescribir métodos y atributos comunes.
    - Clase Madre (Superclase): La clase original que define características generales.
    - Clase Hija (Subclase): La nueva clase que hereda características y puede añadir o modificar las propias.
    - Sobrescritura de Métodos (Overriding): La clase hija puede redefinir métodos de la clase padre para personalizar su comportamiento.

## 5.4 Beneficios:

    - Estructura Jerárquica: Organiza el código desde lo general a lo específico.
    - Mantenimiento: Cambios en la clase padre se reflejan automáticamente en las hijas.
    - Flexibilidad: Permite extender funcionalidades fácilmente. 
    - super(): Función esencial para invocar métodos de la clase padre desde la hija, especialmente usada en el constructor **__init__**.
    - Herencia Múltiple: Python permite que una clase hija herede de múltiples clases padre, estructurando relaciones complejas.

## 5.5 Herencia en el sistema del Banco
Cómo pruebo todos estos conceptos en el sistema del Banco.? <br>
[Sistema del Banco](sistemaBanco.md)

## 5.6 Referencias

- https://www.datacamp.com/es/tutorial/python-inheritance
- https://ellibrodepython.com/herencia-en-python
- https://juncotic.com/poo-herencia-en-python/
- https://oregoom.com/python/herencia/
