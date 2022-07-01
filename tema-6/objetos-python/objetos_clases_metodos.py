class Motor:
    tipo = 'Diesel'

class Ventanas:
    cantidad = '6'

class Ruedas:
    cantidad = '4'

class Carroceria:
    ventanas = Ventanas()
    ruedas = Ruedas()

class Coche:
    motor = Motor()
    carroceria = Carroceria()


c = Coche()
print('Tipo de motor:', c.motor.tipo)
print('Ventanas:', c.carroceria.ventanas.cantidad)
print('Ruedas:', c.carroceria.ruedas.cantidad)
