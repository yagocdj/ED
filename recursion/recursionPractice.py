

def potenciaYago(base, exp) -> int:
    return potenciaAuxiliar(base, 1, exp)


def potenciaAuxiliar(base, exp, limite):
    if exp > limite:
        return 1
    else:
        return base * potenciaAuxiliar(base, exp+1, limite)


'''
1. Há uma regra/padrão que seja geral para a maioria da entrada de dados
   do problema?
   2 ^ 0 = 1
   2 ^ 1 = 2
   2 ^ 2 = 2 x 2
   2 ^ 3 = 2 x 2 x 2
   2 ^ 4 = 2 x 2 x 2 x 2

   base (2) multiplicada n vezes pelo expoente
   se expoente >= 1
   ...
2. Identificar os casos bases
   2 ^ 0  = 1
   O caso base é quem vai determinar a quebra do ciclo de chamadas recursivas

3. Ao começar a desenvolver a solução recursiva, certifique-se que um
   dos argumentos de controle de recursividade está sendo alterado
   a cada chamada recursiva, até que atinja o caso base
'''


def potenciaRecursiva(base, exp, n) -> int:
    print(f'Chamada {n}: base {base}, expoente {exp}')
    if exp == 0:  # caso base
        return 1
    else:
        return base * potenciaRecursiva(base, exp-1, n+1)


def potenciaIterativa(base, exp):
    resultado = 1
    for i in range(exp):
        resultado *= base
    return resultado


def frec(i, j) -> int:
    if i == j:
        return 0
    else:
        return i + frec(i+1, j)


print(frec(2, 6))  # o que será exibido?


def printNumbersDescending(n):
    if n == 0:
        return
    print(n, end=' ')
    printNumbersDescending(n-1)


printNumbersDescending(10)


def printNumbersAscending(n):
    if n == 0:
        return
    printNumbersAscending(n-1)
    print(n, end=' ')


print()
printNumbersAscending(10)


# main
# 2 ^ 4 = 2 x 2 x 2 x 2
print(potenciaIterativa(2, 10))
print(potenciaRecursiva(2, 3, 0))

"""
# Trace de potenciaRecursiva(base, exp, n) -> int

f(base, exp, n) -> subsituí 'potenciaRecursiva' por 'f'

Parâmetros:

base = 2
exp = 3
n = 0 (vai no print)

- chamada 0 -> f(2, 3, 0):
print(...)
exp == 0? False
return 2 * f(2, 2, 1)

- chamada 1 -> f(2, 2, 1):
print(...)
exp == 0? False
return 2 * f(2, 1, 2)

- chamada 2 -> f(2, 1, 2):
print(...)
exp == 0? False
return 2 * f(2, 0, 3)

- chamada 3 -> f(2, 0, 3):
print(...)
exp == 0? True
return 1

- retornos:

f(2, 0, 3) -> return 1
f(2, 1, 2) -> return 2 * 1 = 2
f(2, 2, 1) -> return 2 * 2 = 4
f(2, 3, 0) -> return 2 * 4 = 8

result
f(2, 3, 0) returns int 8
"""

print(potenciaYago(2, 3))

"""
# Trace de potenciaYago(base, exp) -> int

fYago(base, exp)
faux(base, exp, limite)

Parâmetros:

base = 2
exp = limite = 3

- fYago(2, 3):
return faux(2, 1, 3)

- faux(2, 1, 3):
exp > limite? False
return 2 * faux(2, 2, 3)

- faux(2, 2, 3):
exp > limite? False
return 2 * faux(2, 3, 3)

- faux(2, 3, 3):
exp > limite? False
return 2 * faux(2, 4, 3)

- faux(2, 4, 3):
exp > limite? True
return 1

- retornos:

faux(2, 4, 3) -> return 1
faux(2, 3, 3) -> return 2 (2 * 1)
faux(2, 2, 3) -> return 4 (2 * 2)
faux(2, 1, 3) -> return 8 (2 * 4)
fYago(2, 3) -> return 8

result
fYago(2, 3) returns int 8
"""
