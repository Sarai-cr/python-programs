n=int(input ())
m=int(input ())
matriz =[]
contador = 1

if n < 2 or m < 2:
    print ("Error")
else:
    for i in range (n):
        lista=[]
        for x in range (m):
            lista.append(contador)
            contador += 1
        matriz.append(lista)
    print(matriz)



