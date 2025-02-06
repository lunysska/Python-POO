#ejemplos class: funciones continuas

import sympy as sp
class FuncionesContinuas:
    def __init__(self, espresion):
            self.espresion= espresion 
            self.symbol= sp.symbol('x') 

## falta dar esta parte del ejemplo : atributo derivada
            self. derivada= sp.diff (self.espresion, self.symbol)

## los métodos evaluar la funcion y derivar la funcion . 
    def evaluate(self,x_val) :
        return self.espresion.subs (self.symbol, x_val)
    def evaluate_derivada(self,x_val) :
        return self.derivada.subs (self.symbol, x_val)
