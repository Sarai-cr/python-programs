import csv
import math
from funciones_matriz import*

def creaMatriz(nombre_archivo):
    with open(nombre_archivo,newline="") as csv_archivo:
        lector = csv.reader(csv_archivo)
        datos = list(lector)
    return datos 

def columnaNumerica (matriz,numeroDeColumna):
    columna = []
    for i in range (1,len(matriz)):
        if not (matriz [i][numeroDeColumna]):
            dato = 0
        else:
            dato = float (matriz [i][numeroDeColumna])
        columna.append(dato)
    return columna

def suma (matriz, numeroDeColumna):
    listaDeNumeros = obtenDatosFlotantes(numeroDeColumna, matriz)
    return sum(listaDeNumeros)

def titulo(matriz,numeroDeColumna):
    return matriz[0][numeroDeColumna]

def reporte (matriz):
    print("\t\t", end="")
    print ()
    print ("suma:\t")
    for i in range (1,len(matriz[0])):
        print (f"{titulo(matriz,i)}", end ="\t\t")
    print()
    for i in range (1,len(matriz[0])):
        print (f"{math.ceil(suma(matriz,i))}", end ="\t\t")
    print()


def calcularDesviacionEstandar(matriz, numeroDeColumna):
    sumaVarianza = 0.0
    listaDeDatos = obtenDatosFlotantes(numeroDeColumna, matriz)
    promedio = obtenPromedio(listaDeDatos)
    for elemento in listaDeDatos:
        sumaVarianza += math.pow(elemento - promedio, numeroDeColumna)
    return math.pow(sumaVarianza / len(listaDeDatos), 1/2)

def reporteDesviacion(matriz):
    for numeroDeColumna in range (1,6):
        desviacion = calcularDesviacionEstandar(matriz,numeroDeColumna) 
        print ("Desviación Estándar: ", titulo(matriz, numeroDeColumna),desviacion)
        

def calculaPercentiles(matriz,numeroDeColumna,nPercentil):
    numeros = sorted(columnaNumerica(matriz,numeroDeColumna))
    r= round((nPercentil/100)*len(numeros))
    return (numeros[r])

def reportePercentiles(matriz,nPercentil):
    for numeroDeColumna in range (1,6):
        percentiles = calculaPercentiles(matriz,numeroDeColumna,nPercentil) 
        print ("Percentiles: ", titulo(matriz, numeroDeColumna),percentiles)


def calcularModa(matriz,numeroDeColumna):
    listaDeDatos = obtenDatosFlotantes(numeroDeColumna, matriz)
    moda = 0.0
    repeticiones = 0
    for numero in listaDeDatos:
        nuevaRepeticion = listaDeDatos.count(numero)
        if nuevaRepeticion > repeticiones:
            moda = numero
            repeticiones = nuevaRepeticion
    return moda
def reporteModa(matriz):
    for numeroDeColumna in range (1,6):
        moda = calcularModa(matriz,numeroDeColumna) 
        print ("Moda: ", titulo(matriz, numeroDeColumna),moda)


def obtenPromedio(listaDeNumeros):
    return sum(listaDeNumeros) / len(listaDeNumeros)

def valorMaximo(matriz,numeroDeColumna):
    listaDeDatos = obtenDatosFlotantes(numeroDeColumna, matriz)
    return max(listaDeDatos)
def reporteMaximo(matriz):
    for numeroDeColumna in range (1,6):
        valorMax = valorMaximo(matriz,numeroDeColumna) 
        print ("Máximo: ", titulo(matriz, numeroDeColumna),valorMax)

     
def valorMinimo(matriz,numeroDeColumna):
    listaDeDatos = obtenDatosFlotantes(numeroDeColumna, matriz)
    return min(listaDeDatos)
def reporteMinimo(matriz):
    for numeroDeColumna in range (1,6):
        valorMin = valorMinimo(matriz,numeroDeColumna) 
        print ("Mínimo: ", titulo(matriz, numeroDeColumna),valorMin)
        

def columnaDeTexto (matriz,numeroDeColumna):
    columna = []
    for i in range (1,len(matriz)):
        if not (matriz [i][numeroDeColumna]):
            dato = "empty"
        else:
            dato =  (matriz [i][numeroDeColumna])
        columna.append(dato)
    return columna

def damePeliculaMayorIngreso(matriz):
    titulo = ""
    ingreso_m=0
    ingresos = columnaNumerica (matriz,6)
    titulos = columnaDeTexto(matriz,0)
    for i in range (0,len (ingresos)):
        if ingresos[i]>ingreso_m:
            titulo=titulos[i]
            ingreso_m=ingresos[i]
    return titulo

def damePeliculasRango(matriz,inicio,fin):
    lista=[]
    titulos = columnaDeTexto(matriz,0)
    años= columnaNumerica(matriz,1)
    for i in range (0,len (titulos)):
        if años [i] >=inicio and años[1] <= fin:
            lista.append(titulos[i])

    return lista

def tituloMasLargo(matriz):
    lista=[]
    titulo=""
    titulos = columnaDeTexto(matriz,0)
    años= columnaNumerica(matriz,1)
    for i in range (0,len (titulos)):
        if len(titulos[i])>len(titulo):
            lista= matriz[i+1]
            titulo=titulos[i]
    return lista

def gananciasAnuales(matriz):
    ganacias ={}
    años = columnaNumerica(matriz,1)
    ingresos = columnaNumerica(matriz,6)
    for i in range (0,len (años)):
        if años[i] in ganacias:
            ganacias[años[i]]+= round(ingresos[i])
        else:#ingresa por primera vez al diccionario
            ganacias[años[i]]= round(ingresos[i])
    return ganacias