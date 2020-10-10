from statistics import*
import math

edades = [31, 33, 26, 27, 27, 27, 32 , 31, 32, 25, 29, 28, 32, 32, 27, 24, 24, 27, 26, 26, 29, 31, 32, 30, 33]
suma = 0
sumaVarianza= 0
for dato in edades:
    suma += dato
print(" Suma de las edades: ",suma)
promedio = mean(edades)

for edad in edades:
    sumaVarianza += math.pow(edad - promedio, 2)
varianza = len(edades)
desviacionEstandar = math.pow (varianza,0.5)

print (" Promedio: ", promedio)
print (" Varianza: ",sumaVarianza/varianza)
print (" Desviación Estándar: ",desviacionEstandar)

