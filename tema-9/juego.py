import random

numeroCorrecto = random.randint(1, 8)
oportunidades = 3

numero = 0

while numero != numeroCorrecto:
    print(oportunidades)
    numero = int(input('Indique un numero entre el 1 y 8: '))
    oportunidades -= 1
    if oportunidades == 0 and numero != numeroCorrecto:
        print('Perdiste!')
        break
    if numero < numeroCorrecto:
        print('muy bajo')
        continue

    if numero > numeroCorrecto:
        print('muy alto')
        continue

    if numero == numeroCorrecto:
        print('Acertaste!')
        break