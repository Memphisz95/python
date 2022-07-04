f = open('C:/Users/adria/intellij/tema-8/miFichero.txt', 'w')
lista = [
    'primera linea\n',
    'segunda linea\n'
]
f.writelines(lista)
f.close()