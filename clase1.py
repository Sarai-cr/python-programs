import random

dado = random.randint(1,6) #a diferencia del range, si incluye el 6
print (dado)
print ("------")
lista = []
for i in range (20):
     dado = random.randint(1,6)
     lista.append(dado)
print (lista)
print ("-------")
matriz = []
for i in range (5):
    renglon = []
    for j in range (5):
        dado = random.randint(1,100)
        renglon.append(dado)
    matriz.append(renglon)
print (matriz)
