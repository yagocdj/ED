from Baralho import Baralho
from Carta import Carta


def embaralhar():
    print('função embaralhar()')


embaralhar()

c = Carta('2', 'espada', 'vermelho')
c.valor = 'rei'
print(c)

baralho = Baralho(True)
# baralho.embaralhar()
print(baralho)

"""
for i in range(53):
    print(baralho.retirarCarta())
"""

while (baralho.temCarta()):
    carta = (baralho.retirarCarta())
    print(carta)

print('Não há mais cartas a serem retiradas.')
print('Total de cartas no baralho', len(baralho))

baralho.receberCarta(carta)
baralho.receberCarta(carta)

print('Total de cartas no baralho:', len(baralho))
print(baralho)

baralho2 = Baralho()

for i in range(42):
    baralho2.retirarCarta()

print('Baralho 2\n')
print(baralho2)

print('Fazer o baralho 1 receber as cartas do baralho 2')
baralho.juntarBaralho(baralho2)
print(baralho)
print(len(baralho))
print(len(baralho2))

'''
alunos = {10: 'Lucas', 11: 'Luis', 12: 'Yago'}
baralho.container.append(alunos)
print(baralho)
'''

"""
input()

print(baralho)

embaralhar()
"""
