
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

        

    
        

