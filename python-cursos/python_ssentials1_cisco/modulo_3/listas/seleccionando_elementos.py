#Crea un algoritmo donde se pueda seleccionar cualquier elemento de una lista ya declarada con mas de 5 elementos
#Si deseas puedes pedir al usuario estos elementos y despues almacenarlos en una lista
#considera si le piedes al usuario ingresar los elementos que tendran la lista, tambien que le pida que cantidad de datos a almacenar
#Considera que el algoritmo tambien tiene que darle la opcion de modificar, eliminar o seguir agregando los elementos de la lista en caso lo queira el usuario

memory_list = []
num_elements = int(input("Cuantos elementos desea ingresar:"))

for i in range(num_elements):
    element = input(f"por favor ingrese el elemento {i+1}: ")
    memory_list.append(element)

print(memory_list)

modify = input("Desea modificar algun elemento de la lista? (si/no): ").lower()
if modify == "si":
    print(f"Los elementos de su lista son {len(memory_list)}")
    for i in range(len(memory_list)):
        print(f"Elemento {i+1}: {memory_list[i]}")
    elemetn_to_modify = input("Que elemento de la lista desea modificar?\nIngrese el numero o nombre del elemento: ")

if (elemetn_to_modify in memory_list) or (memory_list[int(elemetn_to_modify)-1] in memory_list):#corregir error de evaluacion, no evalua error de typeo
    for i in range(len(memory_list)):
        if memory_list[i] == elemetn_to_modify or i == int(elemetn_to_modify)-1:
            elemetn_to_modify = i
        continue
    new_element = input(f"Ingrese la modificacion del elemento '{memory_list[elemetn_to_modify]}': ")
    memory_list[elemetn_to_modify] = new_element
    print(memory_list)