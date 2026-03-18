''' 
Created on March,2026 
@author: lunysska

'''

Este ejemplo muestra cómo se puede usar las concidicionales para validar entradas de datos.
El principal objetivo de este ejemplo es mostrar cómo usarlos en Principios de Diseño
Las validaciones en componentes Entidad (especializados para representar componentes básicos, de manejo de datos) van con valores booleanos y la comunicación con los clientes va sólo en componentes de Contacto (especializados para comunicarse con el Usuario)

El ejemplo se muestra así:
1. En la clase Cuenta, en el método retirar, se valida la entrada, pero se regresa valores booleanos
2. En la clase Menu, cuando se usa ese método, se verifican los valores booleanos y entonces ya se regresan mensajes adecuados para el Usuario
