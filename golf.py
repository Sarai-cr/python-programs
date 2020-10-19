n = int(input())


for x in range(0,n):
    p = int(input())
    s = int(input())
    if p - s == 1:
        print('Birdie')
    elif s - p == 1:
        print('Bogye')
    elif p - s == 2:
        if p == 3:
            print ("Hole in one")
        else:
            print('Eagle')
    
    elif s - p >=  2 and s - p < 20:
       print('Double Bogye')
    
    elif s == 1:
        print('Hole in one')
    elif p == s:
        print('Par')
    else:
        if s >= 20:
            print('Mal jugador')