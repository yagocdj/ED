from filaSequencialCircular import *


fila = Fila(10)
# teste do vazia
if fila.estaVazia():
    print('Fila está vazia')
# tesde do cheia
if fila.estaCheia():
    print('Fila está cheia')
# tamanho da fila
print('Tamanho: ', len(fila))
# consultando por elemento
try:
    for i in range(10):
        fila.enfileira(f'aluno{i+1}')

    print(fila)

    print("Busca (aluno5):", fila.busca('aluno5'))
    print('Elemento 10:', fila.elemento(10))
    print()

    fila.esvazia()
    print(fila)
    print('Tamanho: ', len(fila))


except FilaException as fe:
    print(fe)

novaFila = Fila(7)

try:

    print(novaFila)

    novaFila.enfileira(1)
    novaFila.enfileira(3)
    novaFila.enfileira(5)
    novaFila.enfileira(7)
    novaFila.enfileira(9)
    novaFila.enfileira(8)

    print(novaFila)

    novaFila.desenfileira()

    print(novaFila)

    novaFila.enfileira(11)

    print(novaFila)

except FilaException as fe:
    print(fe)
