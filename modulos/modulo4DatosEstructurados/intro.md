# 4. Datos estructurados

## 4.1. Encapsulamiento en PPOO. (Público vs privado)

El **encapsulamiento** en Python es un pilar de la Programación Orientada a Objetos (POO) que restringe el acceso directo a los atributos y métodos de una clase para evitar modificaciones accidentales. Se logra mediante convenciones de nombres: un guion bajo **_** para miembros protegidos y doble guión bajo **__** para privados, limitando su visibilidad externa. 

Principales conceptos de Encapsulamiento en Python:

    - Público (Por defecto): Los atributos y métodos son accesibles desde fuera de la clase.
    - Protegido (_variable): Se usa un guion bajo antes del nombre. Es una convención que indica que el miembro no debe ser accedido directamente fuera de la clase o subclases, pero Python no impide el acceso.
    - Privado (__variable): Se usan dos guiones bajos. Python cambia el nombre del atributo internamente (name mangling) para dificultar su acceso directo desde fuera, lanzando un AttributeError si se intenta.
    - Getters y Setters: Métodos públicos utilizados para obtener (get) o modificar (set) el valor de atributos privados o protegidos de forma segura. 

``` python
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular        # Público
        self.__saldo = saldo          # Privado (doble guion bajo)

    # Getter para saldo 
    def get_saldo(self): # o getSaldo(self):
        return self.__saldo

    # Setter para saldo con validación
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return True
        else:
            return False

cuenta = CuentaBancaria("Juan", 1000)
# print(cuenta.__saldo)  # Esto generaría un AttributeError
print(cuenta.get_saldo())  # Forma correcta (salida: 1000)
cuenta.depositar(500)
print(cuenta.get_saldo())
```

### Beneficios:

    Seguridad: Protege la integridad de los datos internos de los objetos.
    Modularidad: Permite cambiar la implementación interna sin afectar el código externo que utiliza la clase.
    Control: Facilita la validación de datos al modificar atributos a través de métodos setters.

[Ejercicios](ejercicio1-publicoVsPrivado/README.md)


## Referencias
- https://www.datacamp.com/es/tutorial/encapsulation-in-python-object-oriented-programming
- https://ellibrodepython.com/encapsulamiento-poo
- https://repositorio-uapa.cuaed.unam.mx/repositorio/moodle/pluginfile.php/3076/mod_resource/content/1/UAPA-Abstraccion-Encapsulamiento/index.html
