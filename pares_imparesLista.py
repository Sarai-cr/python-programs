entrada = input ()
listaDeNumeros = []
pares = 0
impares= 0

while entrada != "*":
    listaDeNumeros.append(int(entrada))
    entrada =  input ()



for numero in listaDeNumeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print ("PARES=",pares)
print ("IMPARES=",impares)

        
