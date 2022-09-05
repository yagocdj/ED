from pais import Pais

p1 = Pais('Brasil', 'Brasilia', 4000.0)
p2 = Pais('Argentina', 'Buenos Aires', 4000.0)

print(p1)
print(p2)

print(p1.vizinhos)
print(p2.capital)

p1.addPaisDeFronteira('Uruguai')
p1.addPaisDeFronteira('Argentina')
p1.addPaisDeFronteira('Paraguai')
p1.addPaisDeFronteira('Peru')
p1.addPaisDeFronteira('Peru')

print(p1.vizinhos)
