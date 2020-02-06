paises = ['argentina', 'brasil', 'uruguay']
print(paises)

paises.sort(reverse=True)
print(paises)

paises.append('colombia')
print(paises)

paises.insert(2, 'ecuador')
print(paises)

del paises[2]
print(paises)

pais_borrado = paises.pop(len(paises)-1)
print("Borré a " + pais_borrado)
print(paises)

paises.remove('brasil')
paises.reverse()
print(paises)
