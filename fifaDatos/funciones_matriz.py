
import math

def obtenColumnaDeMatriz(numeroDeColumna, matriz):
    columna = []
    for renglon in matriz:
        columna.append(renglon[numeroDeColumna])
    return columna

def convierteListaDeCadenasAFlotante(listaDeCadenas):
    listaDeNumeros = []
    for cadena in listaDeCadenas:
        listaDeNumeros.append(
            float(validaCadenaVacia(cadena))
        )
    return listaDeNumeros

def validaCadenaVacia(cadena):
    if cadena == "":
        return "0"
    else:
        return cadena

def obtenDatosFlotantes(numeroDeColumna, matriz):
    return(
        convierteListaDeCadenasAFlotante(
            obtenColumnaDeMatriz(numeroDeColumna, matriz)[numeroDeColumna:]
        )
    )

def obtenIndicePorNombre(nombre, matriz):
    titulos = matriz[0]
    for indice in range( len(titulos) ):
        if nombre == titulos[indice]:
            return indice

def obtenDatosEnPies(numeroDeColumna, matriz):
    listaDeFlotantes = []
    for cadena in obtenColumnaDeMatriz(numeroDeColumna, matriz)[1:]:
        listaDeFlotantes.append( leePies(cadena) )
    return listaDeFlotantes

def obtenDatosEnLibras(numeroDeColumna, matriz):
    listaDeFlotantes = []
    for cadena in obtenColumnaDeMatriz(numeroDeColumna, matriz)[1:]:
        listaDeFlotantes.append( leeLibras(cadena) )
    return listaDeFlotantes

def leePies(cadena):
    if cadena:
        separa = cadena.split("'")
        parteEntera = float( validaCadenaVacia(separa[0]) )
        parteDecimal = float( validaCadenaVacia(separa[1]) ) / (math.pow(10, len(separa[1])))
        return parteEntera + parteDecimal
    else:
        return 0.0

def leeLibras(cadena):
    if cadena:
        return float( cadena.replace("lbs", "") )
    else:
        return 0.0