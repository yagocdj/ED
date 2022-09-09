from PilhaSequencial import Pilha

userChoice = ''

while userChoice != 'sair':
    allStacks = [Pilha()]
    currentStack = 0
    allStacks[currentStack].empilha(10)
    allStacks[currentStack].empilha(20)
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
    userChoice = input('Digite a sua opção: ')
    # TERMINAR ESTE PROGRAMA
