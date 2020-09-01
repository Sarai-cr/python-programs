def bisiesto (año):
    if año % 4 == 0:
        if año % 100 == 0 and año % 400 == 0:
            return True
        elif año % 100 == 0:
            return False
        else:
            return True
    return False

year = int (input ())

esBisiesto = bisiesto(year)
print(esBisiesto)