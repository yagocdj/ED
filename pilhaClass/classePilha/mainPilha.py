from PilhaSequencial import Pilha, PilhaException

numeros = [4,5,6,90,56,31,42,57]
print(numeros)

pilha = Pilha()

for n in numeros:
    pilha.empilha(n)

print('Array:', numeros)
print('Pilha', pilha)

string = 'Instituto Federal da Paraíba'
pilha.esvazia()
for s in string:
    pilha.empilha(s)

while (not pilha.estaVazia()):
    print(pilha.desempilha(), end='')
try:
    pilha.busca(90)
except PilhaException as pe:
    print(pe)
