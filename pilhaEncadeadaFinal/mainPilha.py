from PilhaEncadeada import *

numeros = [4, 5, 6, 90, 56, 31, 42, 57]

pilha = Pilha()
for n in numeros:
    pilha.empilha(n)

print('Array: ', numeros)
print('Pilha: ', pilha)
print('Sub-topo: ', pilha.subTopo())

string = 'Instituto Federal da Paraiba'
pilha.esvazia()
print(string)
for s in string:
    pilha.empilha(s)
print()

while(not pilha.estaVazia()):
    print(pilha.desempilha(), end='')

print()

try:
    print
    print(pilha.busca(90))
except PilhaException as pe:
    print(pe)

numerosDobrados = [numero * 2 for numero in numeros]
pilhaDobro = Pilha()

for value in numerosDobrados:
    pilhaDobro.empilha(value)

print(pilhaDobro)
print(pilhaDobro.desempilha_n(6))
print(pilhaDobro)
