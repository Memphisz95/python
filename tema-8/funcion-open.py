f = open('C:/Users/adria/MiModulo.Java', 'r')

def main():
    usuarios = listaUsuarios()
    print(usuarios)

def listaUsuarios():
    f = open('C:/Users/adria/MiModulo.Java', 'r')
    datos = f.readlines()
    f.close()

    for linea in datos:
        if linea[0] == '*':
            continue
        print(linea)

if __name__ == '__main__':
    main()

# r: leer
# a: append
# w: escritura
# x: create

# t: texto
# b: binary

# + --> abierto escritura y lectura