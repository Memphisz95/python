numero_inicial = int(input('Indique un numero inicial: '))
numero_final = int(input('Indique un numero final: '))

while numero_inicial < numero_final:
    numero_inicial += 1
    if numero_inicial % 2 != 0:
        print(numero_inicial)