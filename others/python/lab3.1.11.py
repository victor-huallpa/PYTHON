# si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal).
# si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del excedente sobre 85,528 pesos.

income = float(input("Introduce el ingreso anual: "))

if income < 85528 and income > 0:
	tax = income * 0.18 - 556.02
# Escribe tu código aquí.
else :
	tax = income - (14839.02 + 0.32*(income - 85528)) 
tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
 