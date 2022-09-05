from carta import Carta
from baralho import Baralho

def embaralhar():
    print('Função embaralhar()')

embaralhar()
baralho = Baralho()
baralho.embaralhar()

"""
c1 = Carta('4', 'espada', 'preto')
c2 = Carta('Dama', 'ouro', 'vermelho')
print(c1.__dict__)
embaralhar()

print(c1)
print(c2)
print(c1.getNaipe())
c1.naipe = 'Jupiter' # modifica o atributo naipe caso ele esteja público
print(c1.naipe) # retorna um erro pois esse atributo está privado
print(c1)
"""

print(baralho)
print(len(baralho))

baralho.embaralhar()
input()

print(baralho)
