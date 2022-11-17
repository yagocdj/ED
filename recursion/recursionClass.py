from typing import List


def n_numbers(n):
    '''exibe na tela os números de 0 até n'''
    if n < 0:
        return
    n_numbers(n-1)
    print(n, end=' ')


def soma(a, b) -> int:
    '''Somar os numeros no intervalo fechado de "a" a "b"'''
    if a == b:
        return a
    else:
        return a + soma(a+1, b)


def strlen(str) -> int:
    if len(str) == 0:
        return 0
    else:
        return 1 + strlen(str[1:])


"""
# Trace de strlen(str) -> int

str = 'IFPB'

chamada 1 - strlen('IFPB')
len('IFPB') == 0? False
return 1 + strlen('FPB')

chamada 2 - strlen('FPB')
len('FPB') == 0? False
return 1 + strlen('PB')

chamada 3 - strlen('PB')
len('PB') == 0? False
return 1 + strlen('B')

chamada 4 - strlen('B')
len('B') == 0? False
return 1 + strlen('')

chamada 5 - strlen('')
len('') == 0? True
return 0

retornos

strlen('') returns 0
strlen('B') returns 1 (1+0)
strlen('PB') returns 2 (1+1)
strlen('FPB') returns 3 (2+1)
strlen('IFPB') returns 4 (3+1)
"""


def strlenaux(str) -> int:
    return strlen2(str, 0)


def strlen2(str, i=0) -> int:
    if i == len(str):
        return 0
    else:
        return 1 + strlen2(str, i+1)


def maior(array) -> float:
    if len(array) == 0:
        raise Exception('Array vazio.')
    if len(array) == 1:
        return array[0]
    return max(array[0], maior(array[1:]))
    '''
    retorno = maior(array[1:])
    if array[0] > retorno:
        return array[0]
    else:
        return retorno
    '''


def printStr(string, i=0) -> None:
    if i == len(string):
        return
    print(string[i], end='')
    printStr(string, i+1)


def printStr2(string: str) -> None:
    if len(string) == 0:
        return
    print(string[0], end='')
    printStr2(string[1:])


# it's name was invertString
def reverseString(string: str) -> str:
    if len(string) == 1:
        return string[0]
    return reverseString(string[1:]) + string[0]


def printInverse(string):
    if len(string) == 0:
        return
    printInverse(string[1:])
    print(string[0], end='')


def compareStr(string_one: str, string_two: str) -> int:
    if len(string_one) == len(string_two):
        return 0
    if len(string_one) == 0:
        return -1
    if len(string_two) == 0:
        return 1
    return compareStr(string_one[1:], string_two[1:])


def n_integers_sum(n: int) -> int:
    if n < 0:
        raise Exception('The argument "n" is smaller than 0')
    if n == 0:
        return 0
    return n + n_integers_sum(n-1)


def menores_rec(numbers_list: List[int], key: int) -> int:
    if len(numbers_list) == 0:
        return 0
    if key > numbers_list[0]:
        return 1 + menores_rec(numbers_list[1:], key)
    else:
        return menores_rec(numbers_list[1:], key)


def decToBin(number: int):
    if number // 2 == 0:
        print(number % 2, end='')
        return
    decToBin(number // 2)
    print(number % 2, end='')


def ispalindrome(string: str):
    normal_string = reverseString(string)
    reverse_string = string
    return normal_string == reverse_string
    """ reverse_str = ispalindrome(string[1:]) + string[0]
    normal_str = string[0] + ispalindrome(string[1:]) """


def invictus(mass: float):
    return invictusAux(mass, 0)


def invictusAux(mass: float, time: int):
    if mass < 0.8:
        return time, mass
    if time % 50 == 0:
        return invictusAux(mass / 2, time+1)
    else:
        return invictusAux(mass, time+1)


def seqTermos1(n: int):
    if n < 1:
        raise Exception('The integer n must be greater than 0.')
    if n == 1:
        return 1
    return 1/n + seqTermos1(n-1)


def seqTermos2(n: int):
    if n < 0:
        raise Exception('The integer n must be greater than 0.')
    if n == 0:
        return 0
    return (n**2 + 1) / (n+3) + seqTermos2(n-1)


def isSorted(array: list) -> bool:
    if len(array) == 1:
        return True
    for i in range(1, len(array)):
        if array[i] < array[0]:
            return False
    return isSorted(array[1:])


"""
# Trace de maior(array) -> float

arr = [1.3, 1.9, 2.1, 3.0]

chamada 1 - maior([1.3, 1.9, 2.1, 3.0])
len([1.3, 1.9, 2.1, 3.0]) == 0? False
len([1.3, 1.9, 2.1, 3.0]) == 1? False
return max(1.3, maior([1.9, 2.1, 3.0]))

chamada 2 - maior([1.9, 2.1, 3.0])
len([1.9, 2.1, 3.0]) == 0? False
len([1.9, 2.1, 3.0]) == 1? False
return max(1.9, maior([2.1, 3.0]))

chamada 3 - maior([2.1, 3.0])
len([2.1, 3.0]) == 0? False
len([2.1, 3.0]) == 1? False
return max(2.1, maior([3.0]))

chamada 4 - maior([3.0])
len([3.0]) == 0? False
len([3.0]) == 1? True
return 3.0

retornos

maior([3.0]) returns 3.0
maior([2.1, 3.0]) returns 3.0
maior([1.9, 2.1, 3.0]) returns 3.0
maior([1.3, 1.9, 2.1, 3.0]) returns 3.0

"""

# programa principal

# rating = [4.5, 13.2, 2.8, 4.9, 5.0, 2.6]
# print('Maior: ', maior(rating))
# print()
# print('strlen(): ', strlen('ifpb'))
# print('strlen2(): ', strlen2('ifpb', 2))

# print()
# n = 10
# n_numbers(n)
# print('Soma: ', soma(2, 5))

# printStr2('Pão doce')
# print(invertString('Yago'))
# print(invertString('Hello, world!'))
# print(invertString('Zap'))
# printInverse('Olá, mundo!')
# print(n_integers_sum(-1))
# print(n_integers_sum(3))
# my_numbers = [10, 15, 13, 9, 1, 4, 2]
# my_key = 5
# print(menores_rec(my_numbers, my_key))

# decToBin(192)
# print(ispalindrome('arara'))  # True
# print(ispalindrome('carro'))  # False
# print(ispalindrome('mamam'))  # True

# print(compareStr('maçã', 'pera'))
# print(compareStr('cerveja', 'sabão'))
# print(compareStr('valor', 'algoritmos'))

# print(seqTermos1(5))
# print(seqTermos1(2))
# print(seqTermos1(1))
# print(seqTermos1(-1))

# print(seqTermos2(5))
# print(seqTermos2(2))
# print(seqTermos2(1))
# print(seqTermos2(-1))

# print(invictus(10))

print(isSorted([1, 2, 3, 4]))  # True
print(isSorted([10, 1, 2, 1, 3, 9, 5]))  # False
print(isSorted([10, 15, 20]))  # True
print(isSorted([1, 10, 3, 5]))  # False
print(isSorted([1]))  # True
print(isSorted([1, -1]))  # False
