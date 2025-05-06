# Paso 1: Solicitar al usuario el número de elementos de la serie
n = int(input("¿Cuántos números de la serie de Fibonacci deseas mostrar? "))

# Paso 2: Inicializar los dos primeros valores de la serie
a = 0
b = 1

# Paso 3: Usar un bucle for desde 0 hasta n-1
print("Serie de Fibonacci:")
for i in range(n):
    print(a)          # Mostrar el número actual
    c = a + b         # Calcular el siguiente número
    a = b             # Actualizar a al siguiente valor
    b = c             # Actualizar b al siguiente valor
