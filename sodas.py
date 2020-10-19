precio = int (input ())
dinero = int (input ())
cambio = 0

if precio < 0 or dinero < 0:
    print ("NOT VALID THOONY")
elif precio > dinero:
    print ("INSUFICIENTE THOONY")
else:
    cambio = dinero - precio
    print (cambio)

aux = 1 
while cambio > 0 :
    print (f' {cambio % 10} x {aux}')
    cambio = cambio //10
    aux = aux * 10
    


 