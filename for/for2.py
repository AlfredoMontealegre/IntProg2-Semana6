# Leer un numero ingresado por el usuario
# Mostrar la letra a por cada numero del 1 - al numero
# Ingresado por el usuario, ejemplo: Numero: 3
# a 
# aa
# aaa

def mostrarLetra(numero):
    for i in range(numero):
        print(f"a"*numero)

def main():
    num = int(input("Ingresa un numero: "))
    mostrarLetra(num)

main()