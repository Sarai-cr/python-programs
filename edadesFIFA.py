from statistics import*
import math

#1.- Abrir archivo

archivo= open ("FIFA.csv", "r")

#2.- Leer archivo

#contenido= archivo.read() #leer archivo en una sola línea
##print (contenido)

#print ("---------------------------")

#contenido= archivo.readline()
##print (contenido)

#Leer una lista de cadenas
contenido= archivo.readlines()
#print (contenido)
#print ("---------------------------")

#3.-Cerrar archivo

archivo.close()
#archivo.readline()



#4.-Procesar datos

#print (contenido[0])
#print (contenido[1])

#print ("---------------------------")

#5.-Crear matriz

matriz=[]
for i in range (1,len(contenido)):
    #print (i,contenido[i])
    renglon=contenido[i].split(",")
    #print(renglon)
    matriz.append(renglon)
#print ("Matriz---------------------")
#print (matriz)

#print ("---------------------------")
#6.-Obtener datos de una columna
renglon = matriz [0]
#print (renglon)
#print (renglon[2])

columna= []
for renglon in matriz:
    dato =int(renglon[3])
    columna.append(dato)
    ##print(dato)

#Operaciones con datos
#print ("---------------------------")
#print ("Suma edades",sum(columna))
#print ("Promedio edades",sum(columna)/len(columna))

def calcularDesviacionEstandar(listaDeDatos):
    sumaVarianza = 0.0
    promedio = mean(listaDeDatos)
    for elemento in listaDeDatos:
        sumaVarianza += math.pow(elemento - promedio, 2)
    return math.pow(sumaVarianza / len(listaDeDatos), 1/2)

print ("Suma edades:",sum(columna))
print ("Promedio edades:",sum(columna)/len(columna))
print( "Desviación Estándar:", calcularDesviacionEstandar(columna) )