# Fibonacci Actualizado
num = int(input("Ingrese un numero: "))
a = 0
b = 1
# Aplicamos el For
for i in range(num):
    print(a)
    c = a + b
    a = b
    b = c