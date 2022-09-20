from PilhaSequencial import *
#from PilhaEncadeada import *
p1 = Pilha()
p2 = Pilha()

for i in range(1,20,3):
    p1.empilha(i)

for i in range(30,36):
    p2.empilha(i)

print('P1:', p1)
print('P2:', p2)

p1.concatena(p2)

print('Concatenacao P2 em P1')
print('P1:', p1)
print('P2:', p2)

p2.concatena(p1)
print('Concatenacao P1 em P2')
print('P1:', p1)
print('P2:', p2)