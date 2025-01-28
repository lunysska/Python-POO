Este es un ejemplo para crear una carpeta dentro del repositorio 
# Ejemplo Objet0: Circulo , clase, atributos y métodos.

# Objeto
class Circulo: 
    def __init__(self,radio):
        self.radio = radio
        
    def area(self):
        return 3.1416 * self.radio **2
    
    def circunferencia(self):
        return 2*3.1416*self.radio
        
    # crear una instancia de la clase Circulo
mi_circulo = Circulo(5)

print(f'Área:{mi_circulo.area()}')

print(f'Circunferencia:{mi_circulo.circunferencia()}')
    


