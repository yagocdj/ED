from filaEncadeada import *


myStack = Fila()
print(myStack.estaVazia())

try:
    myStack.enfileira('A')
    myStack.enfileira('B')
    myStack.enfileira('C')
    myStack.enfileira('D')
    myStack.enfileira(1)

    print(myStack)
    print(myStack.desenfileira())
    print(myStack)

    myStack.esvazia()

    print(myStack)

except FilaException as fe:
    print(fe)
