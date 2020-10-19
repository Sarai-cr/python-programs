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

#def gananciasAnualesBar (ganacias):
    años = list(ganacias.keys())
    acumulados =list (ganacias.values())
    for i in range (0,len(acumulados)):
        plt.bar(i,acumulados[i],tick_label=str(años[i]))
    #plt.xticks(range (0,len(años),años))

    plt.savefig("gananciasBar.png")


#def gananciasAnualesLine (ganacias):
    #años = list(ganacias.keys())
    #acumulados =list (ganacias.values())
    #plt.plot(años,acumulados)
    #plt.savefig("gananciasBar.png")

def añoMayorIngreso (matriz):
    año = ""
    ingreso_m=0
    ingresos = columnaNumerica (matriz,6)
    años = columnaDeTexto(matriz,1)
    for i in range (1,len (ingresos)):
        if ingresos[i]>ingreso_m:
            año=años[i]
            ingreso_m=ingresos[i]
    return año

def mayorMetaScore (matriz):
    listaDeDatos = obtenDatosFlotantes(4, matriz)
    mayorMeta= listaDeDatos.index(max(listaDeDatos))
    return columnaDeTexto(matriz,0)[mayorMeta]

def añosUnicos (matriz):
    columnaAños = obtenColumnaDeMatriz (1,matriz)[1:]
    return list(set(columnaAños))

def decadas (añosUnicos):
    decadas = [ ]
    for año in añosUnicos:
        decadas.append(año[0:-1])
    return list(set(decadas))

def ganaciasPorDecada(matriz):
    listaDecadas = decadas(añosUnicos(matriz))
    años = obtenColumnaDeMatriz(1, matriz)[1:]
    ganancias = obtenDatosFlotantes(6, matriz)
    decadeEarnings = inicializaDiccionario(listaDecadas)
    for index in range(len(ganancias)):
        decada = años[index][0:-1]
        decadeEarnings[decada] = decadeEarnings[decada] + ganancias[index]
    return decadeEarnings

def inicializaDiccionario(listaDecadas):
    diccionario = {}
    for decada in listaDecadas:
        diccionario[decada] = 0
    return diccionario

def promedioImbPorDecada (decada,matriz):
    imbsPorDecada = []
    listaDecadas = decadas(añosUnicos(matriz))
    años = obtenColumnaDeMatriz(1, matriz)[1:]
    imb = obtenDatosFlotantes(3, matriz)
    decadeEarnings = inicializaDiccionario(listaDecadas)
    for index in range(len(imb)):
        decadaImb = años[index][0:-1]
        if decadaImb == decada:
            imbsPorDecada.append(imb[index])
    #print (imbsPorDecada)
    return obtenPromedio(imbsPorDecada)

def peliculaMayorNumeroDeVotos (matriz):
    listaDeDatos = obtenDatosFlotantes(5, matriz)
    indexOfMaxVotes = listaDeDatos.index(max(listaDeDatos))
    return columnaDeTexto(matriz, 0)[indexOfMaxVotes]


def peliculaMenorNumeroDeVotos (matriz):
    listaDeDatos = obtenDatosFlotantes(5, matriz)
    indexOfMinimunVotes = listaDeDatos.index(min(listaDeDatos))
    return columnaDeTexto(matriz, 0)[indexOfMinimunVotes]




