#1 tijera, 2 papel, 3 piedra

def juego (numeroDeJuegos,eleccionJugador1,eleccionJugador2):
    j1 = evaluar_eleccion(numeroDeJuegos,eleccionJugador1)
    j2 = evaluar_eleccion(numeroDeJuegos,eleccionJugador2)
    if (j1 == 1 and j2 == 1) or (j1 == 2 and j2 == 2) or (j1 ==3 and j2 == 3):
        print (" Empate ")
    elif (j1 == 1 and j2 == 3) or (j1 == 2 and j2 == 1) or ( j1 == 3 and j2 == 2 ):
        print ( "Gana j2" )
    elif (j1 == 1 and j2 == 2 )or (j1 == 3 and j2 == 1) or ( j1 == 2 and j2 == 3  ):
        print (" Gana j1 ")
    


numeroDeJuegos = int (input ())
eleccionJugador1 = int (input ())
eleccionJugador2 = int (input ())
totalDeJuegosGanados = 0    

print (juego(numeroDeJuegos,eleccionJugador1,eleccionJugador2))