# Sept, 2019
# @lunysska
# El ejemplo es para mostrar el uso de paquetes. En este caso: "datetime"
# Este método está creado para validar que un objeto de tipo Fecha es creado de 
# manera correcta
from datetime import datetime

def mimetodo(fecha_str):

	try:
		objetoFecha = datetime.strptime(fecha_str,'%d/%m/%Y')
		return True
	except:
		print("error")
		return False

###################################################################
#Las pruebas
#Pero le falta algo al método ¿qué es?, para adecuarlo a mi clase Fecha
fecha_str = "23/12/0000"
print(mimetodo(fecha_str))