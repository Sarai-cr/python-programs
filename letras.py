listaPalabras = []
listaPalabrasLetra=[]

for palabra in range (5):
    palabras = input ()
    listaPalabras.append(palabras)
letra = input ()

for palabra in listaPalabras:
    if palabra.startswith(letra):
        listaPalabrasLetra.append(palabra)
        
print (listaPalabras)
print (listaPalabrasLetra)


