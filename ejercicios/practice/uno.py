# Practica de el uso de IF
num = int(input("Ingrese un numero: "))
if num % 2 == 0 and num > 0:
    print("Es un numero par y positivo")
elif num % 2 == 0 and num < 0:
    print("Es par, pero negativo")
else:
    print("El numero es impar")