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
