numero = float( input() )
suma = 0
numeros_registrados = 0
promedio = 0.0

while numero >= 0:
    suma += numero
    numeros_registrados += 1
    numero = float( input() )

if numeros_registrados > 0:
    promedio = suma / numeros_registrados

print (promedio)