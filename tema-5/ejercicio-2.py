def numeroPrimo(fin):
    for numero in range(2, fin):
        if fin % numero == 0:
            return str(fin) + ' - no es un numero primo'

    return str(fin) + ' - es un numero primo'

print(numeroPrimo(7))