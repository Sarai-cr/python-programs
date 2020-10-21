from respuestas import*

archivoDatos = "FIFA.csv"

matriz = creaMatriz(archivoDatos)
menu()

a = graficaJugadorMasAlto(matriz)
graficaJugadorMasBajo(matriz)
graficaJugadorMasGordo(matriz)
graficaJugadorMasFlaco(matriz)
graficaJugadorMasAgil(matriz)
graficaJugadorMenosAgil(matriz)
graficaJugadorMasViejo(matriz)
graficaJugadorMasJoven(matriz)