cantidadDeNumeros = int (input())
suma = 0
promedio = 0

for x in range ( cantidadDeNumeros ):
    numerosPromedio = float (input ())
    suma += numerosPromedio
    

if cantidadDeNumeros > 0:
    promedio = suma / cantidadDeNumeros

print(promedio)