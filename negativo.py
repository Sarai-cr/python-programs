numero = int (input ())
contadorDePares = 0

while numero >= 0:
    if numero % 2 ==0:
        contadorDePares += 1
    numero = int (input ())

print ( "Total de pares=",contadorDePares,sep = "")