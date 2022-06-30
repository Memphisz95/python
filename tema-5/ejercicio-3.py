def esBisiesto(año):
    if año % 4 == 0 and año % 100 != 0 or año % 400 == 0:
        return str(año) + ' - es bisiesto'
    else:
        return str(año) + ' - no es bisiesto'

print(esBisiesto(1900))