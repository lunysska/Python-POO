#Por Tania C�rdenas
#Mayo de 2019
#Versi�n 5

#Esta clase es el cimiento del programa, permite reconocer el nombre del art�culo, su precio, adem�s de facilitar a los clientes su c�digo de barras, marca y n�mero de piezas disponibles para que puedan elegir de manera sencilla entre las opciones que ofrece nuestro establecimiento.


class Producto:

  #Constructor
  def __init__ (self, nombre, valor, piezas):
    self.nombre = nombre
    self.precio = valor
    self.piezas = piezas

  #Sobreescribimos el M�todo mostrarDetalles 
  def __str__(self):
  
    cadena = "\nTipo de producto: " + str(self.nombre)
    cadena += "\nPrecio del producto: " + str(self.precio)
    cadena +="\nPiezas disponibles: " + str(self.piezas) 
    return cadena 