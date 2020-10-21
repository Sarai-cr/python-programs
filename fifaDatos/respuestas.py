from funciones import*
import matplotlib.pyplot as plt
import csv

def imprime_menu ():
    print('1. Jugador mas Alto')
    print('2. Jugador mas Bajo')
    print('3. Jugador mas Gordo')
    print('4. Jugador mas Flaco')
    print('5. Jugador mas Agil')
    print('6. Jugador menos Agil')
    print('7. Jugador mas Viejo')
    print('8. Jugador mas joven')
    print('9. Salir')

    
def menu ():
    opcion = 0
    matriz = creaMatriz('FIFA.csv')
    while opcion != 9:
        imprime_menu()
        opcion = int(input("Opción: "))
        if opcion  == 1:
           print (imprimeJugadorMasAlto(matriz))
        elif opcion  == 2:
           print(imprimeJugadorMasBajo(matriz))
        elif opcion  == 3:
           print(imprimeJugadorMasGordo(matriz)) 
        elif opcion  == 4:
            print(imprimeJugadorMasFlaco(matriz))
        elif opcion == 5:
            print(imprimeJugadorMasAgil(matriz))
        elif opcion == 6:
            print(imprimeJugadorMenosAgil(matriz))
        elif opcion  == 7:
            print(imprimeJugadorMasViejo(matriz))
        elif opcion == 8:
            print(imprimeJugadorMasJoven(matriz))
        elif opcion  == 9:
            print("GRACIAS c: !!!")



def imprimeJugadorMasAlto(matriz):
    #Sacamos los indices de las columnas que necesitamos para esta respuesta
    indiceAlturas = obtenIndicePorNombre("Height", matriz)
    indiceNombres = obtenIndicePorNombre("Name", matriz)
    #obtenemos los datos de las columnas dados los indices
    alturas = obtenDatosEnPies(indiceAlturas, matriz)
    nombres = obtenColumnaDeMatriz(indiceNombres, matriz)[1:]
    #sacamos la altura maxima
    alturaMaxima = max(alturas)
    #buscamos las posiciones en las alturas que tengan la altura maxima
    indicesAlturaMax = indicesDadoUnValor(alturaMaxima, alturas)
    #obtenemos los nombres de los jugadores dados sus indices
    jugadoresMasAltos = []
    for indice in  indicesAlturaMax:
        jugadoresMasAltos.append( nombres[indice] )
    print(jugadoresMasAltos)
    return jugadoresMasAltos, [alturaMaxima for i in range(len(jugadoresMasAltos))]

def graficaJugadorMasAlto(matriz):
    x,y = imprimeJugadorMasAlto(matriz)
    plt.bar(x,y)
    plt.xlabel('Jugadores')
    plt.ylabel('Estatura [ft]')
    plt.title('Jugadores más altos')
    ##plt.xticks(range (0,len(x)),x)
    ##plt.show()
    plt.savefig("GráficaMasAlto.png")


def imprimeJugadorMasBajo(matriz):
    #Sacamos los indices de las columnas que necesitamos para esta respuesta
    indiceAlturas = obtenIndicePorNombre("Height", matriz)
    indiceNombres = obtenIndicePorNombre("Name", matriz)
    #obtenemos los datos de las columnas dados los indices
    alturas = obtenDatosEnPies(indiceAlturas, matriz)
    nombres = obtenColumnaDeMatriz(indiceNombres, matriz)[1:]
    #sacamos la altura maxima
    altutaMinima = min(alturas)
    #buscamos las posiciones en las alturas que tengan la altura maxima
    indicesAlturaMin = indicesDadoUnValor(altutaMinima, alturas)
    #obtenemos los nombres de los jugadores dados sus indices
    jugadoresMasBajos = []
    for indice in  indicesAlturaMin:
        jugadoresMasBajos.append( nombres[indice] )
    print(jugadoresMasBajos)
    return jugadoresMasBajos, [altutaMinima for i in range(len(jugadoresMasBajos))]

def graficaJugadorMasBajo(matriz):
    x,y = imprimeJugadorMasBajo(matriz)
    plt.bar(x,y)
    plt.xlabel('Jugadores')
    plt.ylabel('Estatura [ft]')
    plt.title('Jugadores más bajos')
    ##plt.xticks(range (0,len(x)),x)
    ##plt.show()
    plt.savefig("GráficaMasBajo.png")

def imprimeJugadorMasGordo(matriz):
    indicePeso= obtenIndicePorNombre("Weight",matriz)
    indiceNombres = obtenIndicePorNombre("Name",matriz)
    peso =obtenDatosEnLibras(indicePeso,matriz)
    nombres = obtenColumnaDeMatriz(indiceNombres, matriz)[1:]
    pesoMaximo = max(peso)
    indicesPesoMax= indicesDadoUnValor(pesoMaximo, peso)
    jugadoresMasGordos=[]
    for indice in  indicesPesoMax:
        jugadoresMasGordos.append( nombres[indice] )
    print(jugadoresMasGordos)
    return jugadoresMasGordos, [pesoMaximo for i in range(len(jugadoresMasGordos))]

def graficaJugadorMasGordo(matriz):
    x,y = imprimeJugadorMasGordo(matriz)
    plt.bar(x,y)
    plt.xlabel('Jugadores')
    plt.ylabel('Peso (lb)')
    plt.title('Jugadores más "gordos')
    ##plt.xticks(range (0,len(x)),x)
    ##plt.show()
    plt.savefig("GráficaMasGordo.png")


def imprimeJugadorMasFlaco(matriz):
    indicePeso= obtenIndicePorNombre("Weight",matriz)
    indiceNombres = obtenIndicePorNombre("Name",matriz)
    peso =obtenDatosEnLibras(indicePeso,matriz)
    nombres = obtenColumnaDeMatriz(indiceNombres, matriz)[1:]
    pesoMinimo = min(peso)
    indicesPesoMin= indicesDadoUnValor(pesoMinimo, peso)
    jugadoresMasFlacos=[]
    for indice in  indicesPesoMin:
        jugadoresMasFlacos.append( nombres[indice] )
    print(jugadoresMasFlacos)
    return jugadoresMasFlacos, [pesoMinimo for i in range(len(jugadoresMasFlacos))]

def graficaJugadorMasFlaco(matriz):
    x,y = imprimeJugadorMasFlaco(matriz)
    plt.bar(x,y)
    plt.xlabel('Jugadores')
    plt.ylabel('Peso (lb)')
    plt.title('Jugadores más flacos')
    ##plt.xticks(range (0,len(x)),x)
    ##plt.show()
    plt.savefig("GráficaMasFlaco.png")


def imprimeJugadorMasAgil(matriz):
    indiceAgilidad = obtenIndicePorNombre("Agility",matriz)
    indiceNombres = obtenIndicePorNombre("Name",matriz)
    nombres = obtenColumnaDeMatriz(indiceNombres, matriz)[1:]
    agilidad =  obtenColumnaDeMatriz(indiceAgilidad, matriz)[1:]
    masAgil = max(agilidad)
    indicesMasAgil= indicesDadoUnValor(masAgil, agilidad)
    jugadoresMasAgil=[]
    for indice in  indicesMasAgil:
        jugadoresMasAgil.append( nombres[indice] )
    print(jugadoresMasAgil)
    return jugadoresMasAgil, [masAgil for i in range(len(jugadoresMasAgil))]

def graficaJugadorMasAgil(matriz):
    x,y = imprimeJugadorMasAgil(matriz)
    plt.bar(x,y)
    plt.xlabel('Jugadores')
    plt.ylabel('Agilidad')
    plt.title('Jugadores más ágiles')
    ##plt.xticks(range (0,len(x)),x)
    ##plt.show()
    plt.savefig("GráficaMasAgil.png")

def imprimeJugadorMenosAgil(matriz):
    indiceAgilidad = obtenIndicePorNombre("Agility",matriz)
    indiceNombres = obtenIndicePorNombre("Name",matriz)
    nombres = obtenColumnaDeMatriz(indiceNombres, matriz)[1:]
    agilidad =  obtenColumnaDeMatriz(indiceAgilidad, matriz)[1:]
    menosAgil = min(agilidad)
    indicesMenosAgil= indicesDadoUnValor(menosAgil, agilidad)
    jugadoresMenosAgil=[]
    for indice in  indicesMenosAgil:
        jugadoresMenosAgil.append( nombres[indice] )
    print(jugadoresMenosAgil)
    return jugadoresMenosAgil, [menosAgil for i in range(len(jugadoresMenosAgil))]

    
def graficaJugadorMenosAgil(matriz):
    x,y = imprimeJugadorMenosAgil(matriz)
    plt.bar(x,y)
    plt.xlabel('Jugadores')
    plt.ylabel('Agilidad')
    plt.title('Jugadores menos ágiles')
    ##plt.xticks(range (0,len(x)),x)
    ##plt.show()
    plt.savefig("GráficaMenosAgil.png")

def imprimeJugadorMasViejo(matriz):
    indiceEdad = obtenIndicePorNombre("Age",matriz)
    indiceNombres = obtenIndicePorNombre("Name",matriz)
    nombres = obtenColumnaDeMatriz(indiceNombres, matriz)[1:]
    edad =  obtenColumnaDeMatriz(indiceEdad, matriz)[1:]
    masViejo = max(edad)
    indicesMasViejos= indicesDadoUnValor(masViejo, edad)
    jugadoresMasViejos=[]
    for indice in  indicesMasViejos:
        jugadoresMasViejos.append( nombres[indice] )
    print(jugadoresMasViejos)
    return jugadoresMasViejos, [masViejo for i in range(len(jugadoresMasViejos))]

def graficaJugadorMasViejo(matriz):
    x,y = imprimeJugadorMasViejo(matriz)
    plt.bar(x,y)
    plt.xlabel('Jugadores')
    plt.ylabel('Edades')
    plt.title('Jugadores más viejos')
    ##plt.xticks(range (0,len(x)),x)
    ##plt.show()
    plt.savefig("GráficaMasViejo.png")
    
def imprimeJugadorMasJoven(matriz):
    indiceEdad = obtenIndicePorNombre("Age",matriz)
    indiceNombres = obtenIndicePorNombre("Name",matriz)
    nombres = obtenColumnaDeMatriz(indiceNombres, matriz)[1:]
    edad =  obtenColumnaDeMatriz(indiceEdad, matriz)[1:]
    masJoven = min(edad)
    indicesMasJoven = indicesDadoUnValor(masJoven, edad)
    jugadoresMasJovenes=[]
    for indice in  indicesMasJoven:
        jugadoresMasJovenes.append( nombres[indice] )
    print(jugadoresMasJovenes)
    return jugadoresMasJovenes, [masJoven for i in range(len(jugadoresMasJovenes))]

def graficaJugadorMasJoven(matriz):
    x,y = imprimeJugadorMasJoven(matriz)
    plt.bar(x,y)
    plt.xlabel('Jugadores')
    plt.ylabel('Edades')
    plt.title('Jugadores más jóvenes')
    ##plt.xticks(range (0,len(x)),x)
    ##plt.show()
    plt.savefig("GráficaMasJoven.png")
