from functools import reduce

def cuadrado(x):
    return x * x

resultado = map(cuadrado, [1,2,3,4,5,6])
print(list(resultado))

def suma(a, b):
    return a + b

res = reduce(suma, [1,2,3,4,5])
print(res)