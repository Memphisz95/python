class Vehiculo:
    color = None
    ruedas = None
    puertas = None

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    velocidad = None
    cilindrada = None

    def cambiarVelocidad(self, velocidad):
        self.velocidad = velocidad

    def cambiarCilindrada(self, cilindrada):
        self.cilindrada = cilindrada

c = Coche('rojo', '4', '5')
print('Color del coche:', c.color)
print('Cantidad ruedas:', c.ruedas)
print('Cantidad puertas:' , c.puertas)
c.cambiarVelocidad('120 kmh/h')
print('Velocidad el coche:', c.velocidad)
c.cambiarCilindrada('80 CV')
print('Cilindrada del coche:', c.cilindrada)