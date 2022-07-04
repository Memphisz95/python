from functools import reduce

def getImpares(x):
    if x % 2 != 0:
        return True

    return False

numeros = [1, 2, 3, 4, 5 ,6, 7, 8, 9, 10]

impares = filter(getImpares, numeros)
print('La suma total de los impares es: ' + str(reduce(lambda a, b: a + b, impares)))
