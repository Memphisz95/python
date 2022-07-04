import pickle
#SERIALIZAR LOS DATOS

class Coche:
    marca = ''

    def __init__(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

# coche1 = Coche('Ferrari')
# f = open('datos.bin', 'wb')
# pickle.dump(coche1, f)
# f.close()

f = open('datos.bin', 'rb')
ferrari = pickle.load(f)
f.close()

print(type(ferrari))
print(ferrari.getMarca())