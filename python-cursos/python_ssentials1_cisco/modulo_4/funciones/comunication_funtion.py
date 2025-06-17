#Funciones Paramtrizadas: son la manera como se manejan los argumentos pasandos atravez de la funcion
#que despues de argumentos pasan a llamarce parametros de la funcion

def message(number): #al argumento pasado lo nombra como parametro number, esto solo cumple solo dentro de la funcion fuera no existe
    print("Ingresa un número:", number)#imprime mensaje mas parametro
 
number = 1234#variable
message(1)
print(number)#imprime variable


#parametros posicionales: consiste en el orden de los parametros asignados es igual a al oreden de los argumentos pasados
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)
 
introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")