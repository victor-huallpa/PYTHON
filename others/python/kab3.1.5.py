# n = int(input('ingrese un numero: '))
# if n < 100:
#     print('')

#el usuario ingresa tres numero y el sistema detecta cual es el mayor
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

if(number1 > number2 and number1 > number3):
    if(number2 > number3):
 
        todos = number3, number2, number1
                                                                               
    else:

        todos = number2, number3, number1
    
    largest_number = number1

elif(number2 > number3):

    if(number1 > number3 or number1 < number2):
 
        todos = number3, number2, number1
                                                                               
    else:

        todos = number2, number3, number1
    todos = number2, number3, number1
    largest_number = number2
else:
    largest_number = number3

print(largest_number)


