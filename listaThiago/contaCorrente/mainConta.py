from conta import ContaCorrente
from typing import List

'''
a) Escreva um programa para criar dez instancias de ContaCorrente, armazenando-os em
uma list. Os valores para inicialização dos objetos deverão ser lidos do teclado;
'''

listaContas: List[ContaCorrente] = []

for i in range(2):

    numeroDaConta = int(input(f'Nº da conta {i}: '))
    saldoDaConta = float(input(f'Saldo da conta {i}: '))
    nomeDoTitular = input(f'Nome do titular da conta {i}: ')
    conta = ContaCorrente(numeroDaConta, saldoDaConta, nomeDoTitular)
    listaContas.append(conta)

'''
b) Criados os objetos, disponibilize um menu de operações para o usuário. Em um loop, o
programa ficara solicitando ao usuário qual o numero da operação abaixo ele deseja
realizar:
1) Depositar
Ao digitar a opção 1, o programa devera ler o numero da conta e o valor a ser
depositado, e realizar a operação.
2) Sacar
Ao digitar a opção 2, o programa devera ler o numero da conta e o valor a ser
sacado, e realizar a operação, testando se o saque ocorreu ou não.
3) Saldo
Ao digitar a opção 3, o programa devera ler o numero da conta e exibir o seu
saldo.
4) Sair
Ao digitar a opção 4, o programa devera ser encerrado. O loop so será encerrado
quando esta operação for informada.
'''

numeroDaConta = 0
sacou = bool()

while True:

    print('\nEscolha uma das opções abaixo')

    print('''\nDepositar - digite 1
    \rSacar - digite 2
    \rConsultar saldo - digite 3
    \rSair - digite 4''')

    escolhaUsuario = int(input('> '))

    # 1 - depositar
    if escolhaUsuario == 1:
        numeroDaConta = int(input('\nDigite o número da conta > '))
        quantiaDeposito = float(
            input('\nDigite a quantia a ser depositada > R$'))
        for i in range(len(listaContas)):
            if numeroDaConta == listaContas[i].numeroConta:
                listaContas[i].depositarDinheiro(quantiaDeposito)
                break

    # 2 - sacar
    elif escolhaUsuario == 2:
        numeroDaConta = int(input('\nDigite o número da conta > '))
        quantiaSaque = float(input('Digite a quantia a ser sacada > R$'))
        for j in range(len(listaContas)):
            if numeroDaConta == listaContas[j].numeroConta:
                sacou = listaContas[j].sacarDinheiro(quantiaSaque)
                break
            else:
                print('\nNúmero da conta inválido. Recomece a operação.')
                break
        if sacou:
            print(f'\nVocê sacou R${quantiaSaque:.2f}')
        else:
            print('\nSaque mal sucedido: saldo insuficiente.')

    # 3 - consultar saldo
    elif escolhaUsuario == 3:
        numeroDaConta = int(input('\nDigite o número da conta > '))
        for k in range(len(listaContas)):
            if numeroDaConta == listaContas[k].numeroConta:
                print(f'\nSaldo atual: R${listaContas[k].saldo:.2f}')
                break

    # 4 - sair
    else:
        break

print('\nFim da operação')
