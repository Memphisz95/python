from modulos import operaciones

a = 10
b = 5

def sumar():
    return operaciones.suma(a, b)

def restar():
    return operaciones.resta(a, b)

def multiplicar():
    return operaciones.multiplicacion(a, b)

def dividir():
    return operaciones.division(a, b)

if __name__ == '__main__':
    print(str(a) + ' + ' + str(b) + ' = ' + str(sumar()))
    print(str(a) + ' - ' + str(b) + ' = ' + str(restar()))
    print(str(a) + ' x ' + str(b) + ' = ' + str(multiplicar()))
    print(str(a) + ' : ' + str(b) + ' = ' + str(dividir()))