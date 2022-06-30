import math

def areaTriangulo(altura, base):
    return (base * altura) / 2

def areaCirculo(radio):
    return round(math.pi * pow(radio, 2), 2)

print(areaTriangulo(3, 4))
print(areaCirculo(0.5))