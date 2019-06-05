from Producto import*

class Carrito:

  #Constructor. Se inicializa con una lista vac�a.
  def __init__(self):
    self.productos = []

  #M�todo que a�ade productos al carrito.
  def agregar(self, producto):
    self.productos.append(producto) 
  
  #M�todo que muestra detalles.
  def __str__(self):
    cadena = "\nCantidad de productos: " + str(len(self.productos))
    for producto in self.productos: 
      cadena += "\n" + str(producto) 
    return cadena