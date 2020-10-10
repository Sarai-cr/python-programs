cantidadDeNumeros = int (input())
listaDeNumeros = []
listaDeNumerosCuadrado = []


for numero in range (cantidadDeNumeros):
    
    listaDeNumeros.append(int(input()))
print (listaDeNumeros)

for numero in listaDeNumeros:
    cuadrado = numero**2
    listaDeNumerosCuadrado.append(cuadrado)
print (listaDeNumerosCuadrado)