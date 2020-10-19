n=int(input ())
m=int(input ())
matriz =[]


if n != m:
    print ("la matriz no es cuadrada")
else:
    for i in range (n):
        lista=[]
        for x in range (m):
            lista.append(int(input ()))
        matriz.append(lista)

    lista =[]
    for i in range (m):
        lista.append(matriz[i][i])
    print (lista)