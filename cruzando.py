palabra1 = input ()
palabra2 = input ()

def dameMitad(numero):
    return int(numero/2) + (numero%2)

divisor1 = dameMitad(len(palabra1))

p1m1 = palabra1[:divisor1]
p1m2 =palabra1[divisor1:]
print(p1m1)
print(p1m2)

divisor2 = dameMitad(len(palabra2))

p2m1= palabra2[:divisor2]
p2m2= palabra2[divisor2:]
print(p2m1)
print(p2m2)

print (p1m1+p2m2)
print (p1m2+p2m1)