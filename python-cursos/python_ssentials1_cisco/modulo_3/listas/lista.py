#Una lista es la manera como almacenamos no solo un valor si no varios valores dentre de una variable, que se le conoce como lista o array
# my_list = ['elemento', 'elemento2', 'elemento3],...,'elementoN']

#Es mas obtimo para manejar gran cantidad de datos

my_list = ['a', 1, 'hello world', 2]
print(my_list)

#indexado
#el indexado es la manera como seleccionamos elementos de una lista y
#al numero introducido dentro de los parentesis se le conoce como indice
#

print(f"El indice cero de la lista contiene: {my_list[0]}")
my_list[0] = 'B'
print(f"El indice cero de la lista contiene: {my_list[0]}\n")

print(f"El indice uno de la lista contiene: {my_list[1]}")
my_list[1] = my_list[3]
print(f"El indice uno de la lista contiene: {my_list[1]}")

