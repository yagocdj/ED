from filaEncadeada import *
#
#
# myQueue = Fila()
# print(myQueue.estaVazia())
#
# try:
#     myQueue.enfileira('A')
#     myQueue.enfileira('B')
#     myQueue.enfileira('C')
#     myQueue.enfileira('D')
#     myQueue.enfileira(1)
#
#     print(myQueue)
#     print(myQueue.desenfileira())
#     print(myQueue)
#
#     myQueue.esvazia()
#
#     print(myQueue)
#
# except FilaException as fe:
#     print(fe)

queue = Fila()

queue.enfileira(1)
queue.enfileira(3)
queue.enfileira(5)
queue.enfileira(7)
queue.enfileira(9)

print(queue)
elementoBuscado = 5
print(f'O elemento {elementoBuscado} está na posição {queue.busca(elementoBuscado)}')
