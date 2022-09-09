from PilhaSequencial import Pilha, PilhaException

userChoice = ''
userInput = ''
returnElement = ''

while userChoice != 'sair':
    allStacks = [Pilha()]
    currentStack = 0
    # CORRIGIR O ERRO DA LINHA 16
    print(
        f'''
    \rEditor de Pilha v1.2
    \r=====================================
    \rPilha selecionada: {currentStack + 1} de {len(allStacks)}
    \r[{allStacks[currentStack].elemento(0)}] <- topo
    \r=====================================
    \r(e) Empilhar
    \r(d) Desempilhar
    \r(t) Tamanho
    \r(o) Obter elemento do topo
    \r(v) Teste de pilha vazia
    \r(r) Criar nova Pilha
    \r(n) Inverter os elementos da pilha
    \r(z) Esvaziar a pilha
    \r(c) Concatenar duas pilhas
    \r(m) Escolher outra pilha
    \r(n) Conversão dec/bin
    \r(s) Sair
    \r=====================================
    '''
    )
    userChoice = input('Digite a sua opção: ').lower()

    if userChoice == 'e':
        userInput = input('Elemento que você deseja empilhar na pilha: ')
        allStacks[currentStack].empilha(userInput)

    elif userChoice == 'd':
        try:
            userInput = input(
                'Elemento que você deseja desempilhar da pilha: ')
            returnElement = allStacks[currentStack].desempilha()
            print(f'\nElemento {returnElement} removido do topo.')
        except PilhaException as pe:
            print('Erro!', pe)
