listaPaises = set()

verLista = input('¿Desea ver la lista de paises? (si) - (no)')

while verLista == 'no':
    pais = input('Escriba un pais: ')
    listaPaises.add(pais)
    verLista = input('¿Desea ver la lista de paises? (si) - (no)')
    continue

listaPaisesOrdenados = sorted(listaPaises)
print('Listado de paises: ' + ', '.join(listaPaisesOrdenados))
