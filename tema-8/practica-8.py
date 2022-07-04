class Coche:
    marca = ''
    combustible = ''

    def __init__(self, marca, combustible):
        self.marca = marca
        self.combustible  = combustible

    def __str__(self): #SOBRECARGA DE METODOS
        return f'Marca: {self.marca} - Combustible: {self.combustible}'

cadena = '    hola, mi nombre es adriAn'
print(cadena.capitalize())
print(cadena.lower().count('a'))
print(cadena.upper())
numero = '5'
print(numero.isdigit())
print(cadena.strip()) #PARA QUITAR ESPACIOS EN BLANCO
