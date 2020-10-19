añoDeInicio = int(input("Año inicial " ))
numeroDeViajes = int(input("Cantidad de viajes"))
viajeAlFuturo = 0
viajeAlPasado = 0
viajeAlPresente = 0

while numeroDeViajes > 0:
  añoDeViaje = int(input())

  if añoDeViaje > añoDeInicio:
    print("Futuro")
    viajeAlFuturo += 1
    añoDeInicio = añoDeViaje
  elif añoDeViaje < añoDeInicio:
    print("Pasado")
    viajeAlPasado += 1
    añoDeInicio = añoDeViaje
  elif añoDeViaje == añoDeInicio:
    print("Presente")  
    viajeAlPresente+=1
    añoDeInicio = añoDeViaje
  numeroDeViajes -= 1

print(f'viajeAlFuturo = {viajeAlFuturo}')
print(f'viajeAlPasado = {viajeAlPasado}')
print(f'viajeAlPresente = {viajeAlPresente}')