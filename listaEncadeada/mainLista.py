from ListaSimplesmenteEncadeada import *

"""
l1 = Lista()
print(l1)
print('Tamanho: ', len(l1))


l1.inserir(1, 20)
l1.inserir(2, 30)
l1.inserir(1, 40)
print(l1)
print('Tamanho: ', len(l1))


while (not l1.estaVazia()):
    print(l1.remover(1))

"""
# Exercício 1 de lista

user_list = Lista()

TAMANHO = 1
INSERIR = 2
REMOVER = 3
EXIBIR_ELEMENTO = 4
PROCURAR_VALOR = 5
MODIFICAR = 6
SAIR = 7

user_choice = 0

while True:

    print(f"""\n\rLista = {user_list}
    \rEditor de Listas
    \r------------------------
    \r1 – Tamanho
    \r2 – Inserir
    \r3 – Remover
    \r4 – Exibir elemento
    \r5 – Procurar valor
    \r6 – Modificar
    \r7 - Sair
    \rDigite sua opção:
    """)

    user_choice = int(input('> '))

    if user_choice == TAMANHO:
        print(f'\nAtualmente, a lista possui {len(user_list)} elementos.')

    elif user_choice == INSERIR:
        try:
            content = input('\nConteúdo > ')
            position = int(input('Posição > '))
            user_list.inserir(position, content)
        except ListaException as le:
            print('Error:', le)

    elif user_choice == REMOVER:
        try:
            position = int(input('\nPosição > '))
            user_list.remover(position)
        except ListaException as le:
            print('Error:', le)

    elif user_choice == EXIBIR_ELEMENTO:
        try:
            position = int(input('\nPosição > '))
            print(
                f'Elemento cuja posição é {position}: {user_list.elemento(position)}')
        except ListaException as le:
            print('Error:', le)

    elif user_choice == PROCURAR_VALOR:
        try:
            content = input('\nConteúdo > ')
            print(
                f'O elemento {content} está na posição {user_list.busca(content)}')
        except ListaException as le:
            print('Error:', le)

    elif user_choice == MODIFICAR:
        try:
            content = input('\nConteúdo > ')
            position = int(input('Posição > '))
            user_list.modificar(position, content)
        except ListaException as le:
            print('Error:', le)

    elif user_choice == SAIR:
        break

    else:
        print('\nError: digite um valor inteiro entre 1 e 7')
        continue

print('\nFim.')
