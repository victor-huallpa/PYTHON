#crear un algoritmo que calcule que tipo de ñao es bisiesto o comun.

def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False
while True:
# Ejemplo de uso:
    anio = int(input('ingrese el año que desea calcular: '))
    if anio >= 1582:
        print(f'\nel año {anio} esta dentro del calendario gregoriano\n___________________________________\n')
        if es_bisiesto(anio):
            print(f"{anio} es un año bisiesto.")
        else:
            print(f"{anio} no es un año bisiesto.")
    elif anio <1582:
        print (f'el año {anio} no esta dentro del calendario gregoriano mis disculpas')