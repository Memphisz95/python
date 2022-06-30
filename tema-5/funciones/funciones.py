def getNombre(nombre='Adrian'): #parametro por defecto
    print('Hola, ' + nombre + '.')

getNombre()

def suma(a, b):
    print(str(a) + ' + ' + str(b) + ' = ' + str(a + b))

def resta(a, b):
    print(str(a) + ' - ' + str(b) + ' = ' + str(a - b))

a = int(input('Indique el primer numero: '))
b = int(input('Indique el segundo numero: '))

opciones = input('Que desea hacer con esos numeros? Sumar o restar? -> ')
if opciones == 'sumar':
    print('Ha elegido sumar...')
    suma(a, b)
elif opciones == 'restar':
    print('Ha elegido restar...')
    resta(a, b)
else:
    print('La operacion que ha elegido no, esta en esta funcion!')