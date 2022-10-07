from PilhaSequencial import *
import sys


def is_operando(char: str) -> bool:
    char = char.upper()
    if ord(char) >= ord('A') and ord(char) <= ord('Z'):
        return True
    return False


def is_operador(char: str) -> bool:
    if char in '+-*/^':
        return True
    return False


def obter_prioridade(operador: str) -> int:
    if is_operador(operador) or operador == '(':
        prioridades = {
            1: '(',
            2: '+-',
            3: '*/',
            4: '^'
        }

        if operador in prioridades.get(1):
            return 1
        if operador in prioridades.get(2):
            return 2
        if operador in prioridades.get(3):
            return 3
        if operador in prioridades.get(4):
            return 4

    return -1


def infixaParaPosfixa(expressao: str) -> str:
    expressao = expressao.replace(' ', '')
    stack = Pilha()
    output = ''
    for char in expressao:
        if is_operando(char):
            output += char
        elif char == '(':
            stack.empilha(char)
        elif char == ')':
            while stack.topo() != '(':
                output += stack.desempilha()
            stack.desempilha()
        elif is_operador(char):
            while (not stack.estaVazia()) and (obter_prioridade(stack.topo()) >= obter_prioridade(char)):
                output += stack.desempilha()
            stack.empilha(char)

    while not stack.estaVazia():
        output += stack.desempilha()

    return output

# MAIN


count = 0

for line in sys.stdin:
    count += 1
    print(f'Expressão {count}:', infixaParaPosfixa(line))
print('\nfim.')
