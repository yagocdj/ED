from typing import Any, List
# Estrutura da classe e como estarão definidos seus atributos e métodos


class Pilha:
    def __init__(self, elementos: List[Any]) -> None:  # TAD
        self.__dados: List[Any] = elementos

    def estaVazia(self) -> bool:
        return True if len(self.__dados) == 0 else False

    def tamanho(self):
        pass

    def imprime(self):
        self.__dados.sort()
        print(self.__dados.__str__() + ' <- topo')

    def empilha(self, elemento: Any):
        pass

    def desempilha(self):
        pass

    def __str__(self):
        pass
