años = {} #diccionario vacío
grupo = [] #lista
grupo.append("Wazaaa")
#para agregar un dato a un diccionario...
años["Wazaaa"]= 15

print(grupo[0])#dato en una posición
print (años)
#print (años [0]) error, no aplica el indexing
nombre = input("n: ")
for i in range (3):
    if nombre in años:
        print ("Si existe")
        años[nombre] += 5
    else:
        años [nombre]=0
print(alumnos)

#para guardar un dato en un diccionario no es necesario usar el append
#para borrar en elemnto de un diccionario
del alumno