# Revisited For3.py
def mostrarNumeros(inicio=0, fin=0):
    if(inicio < fin):
        for num in range(inicio, fin+1):
            print(num)
    else:
        num = inicio
        while(num >= fin):
            print(num)
            num -= 1

mostrarNumeros(fin=8, inicio=4)