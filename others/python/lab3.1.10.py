#crea un algoritmo que impirma ¡Espatifilo es la mejor planta de todas! si se ingresa ESPATIFILO,
#caso contrario imprime "No, ¡quiero un gran Espatifilo!" s i se eingresa espatifilo.
#de lo contrario imprima Espatifilo!, ¡No [entrada]

texto = input('Ingrese un texto: ')

if(texto == 'ESPATIFILO'):
    print('¡Espatifilo es la mejor planta de todas!')
elif(texto == 'espatifilo'):
    print('Espatifilo!, ¡No')
else:
    print('No, ¡quiero un gran Espatifilo!')