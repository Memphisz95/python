import pickle

class Vehiculo:
    marca = ''
    combustible = ''

    def __init__(self, marca, combustible):
        self.marca = marca
        self.combustible = combustible

    def getDatosCoche(self):
        return f'Marca: {self.marca} - Combustible: {self.combustible}'

coche1 = Vehiculo('ferrari', 'gasolina')
# f = open('datos.bin', 'wb')
# pickle.dump(coche1, f)
# f.close()

f = open('datos.bin', 'rb')
ferrari = pickle.load(f)
f.close()

print(type(ferrari))
print(ferrari.getDatosCoche())