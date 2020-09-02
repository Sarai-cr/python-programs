import math

def divide_hamburguesas (hamburguesas,niños):
    if hamburguesas <= 0 or niños <= 0:
        return -1
    else:
        hamburguesasPorNiño = hamburguesas/niños
        return math.floor (hamburguesasPorNiño)

def sobrantes(hamburguesas,hamburguesasPorNiño,niños):
    sobrante = hamburguesas - (hamburguesasPorNiño * niños)
    return sobrante

    

hamburguesas = int (input ())
niños = int (input ())

hamburguesasPorNiño = divide_hamburguesas (hamburguesas,niños)
print ((hamburguesasPorNiño))
 
sobrante = sobrantes (hamburguesas,hamburguesasPorNiño,niños)
print ((sobrante))

