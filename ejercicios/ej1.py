# Calculadora de tablas de multiplicacion
numero = int(input("Ingrese un numero: "))
# ASI, se determina el rango de un numero a pedir.
for i in range(1,11):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")
