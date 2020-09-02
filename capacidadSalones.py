import math

def salones(alumnosS1,capacidadS1,alumnosS2,capacidadS2):
    esValidoS1 = evaluar_salon(alumnosS1,capacidadS1)
    esValidoS2 = evaluar_salon(alumnosS2,capacidadS2)
    if esValidoS1 == "OK" and esValidoS2 == "OK":
        return "AMBOS OK"
    elif esValidoS1 == "OK":
        return "S1 OK"
    elif esValidoS2 == "OK":
        return "S2 OK"
    elif esValidoS1 == "NO" and esValidoS2 == "NO":
        return "AMBOS NO"
    else:
        return "ERROR"    

def evaluar_salon (alumnos,capacidad):
    if alumnos <= 0 or capacidad <= 0:
        return "ERROR"
    elif alumnos <= math.floor(capacidad/3):
        return "OK"
    else:
        return "NO"

alumnosS1 = int (input())
capacidadS1 = int (input ())
alumnosS2 = int (input ())
capacidadS2 = int (input ())

        
print ( salones (alumnosS1,capacidadS1,alumnosS2,capacidadS2) )