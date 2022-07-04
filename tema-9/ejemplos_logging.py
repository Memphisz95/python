import logging

logging.warning('Esto es un warning')
logging.critical('Esto es un critical')
logging.info('Esto es un info')
logging.error('Esto es un error')

numero = [1, 2, 3, 4, 5]

def mifuncion(x):
    if x % 2 == 0:
        return True

    return False

#FILTER ES UNA FUNCION PARA UNA LISTA, ARRAY, ETC
resultado = filter(mifuncion, numero)
print(list(resultado))