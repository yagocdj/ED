from typing import Any, List


class PilhaException(Exception):
    def __init__(self, msg) -> None:
        super().__init__(msg)


class Pilha:
    def __init__(self) -> None:
        self.__dados: List[Any] = list()
        # caso for a linguagem Java, precisamos da propriedade "topo"

    def estaVazia(self) -> bool:
        return len(self.__dados) == 0

    def tamanho(self) -> int:
        return len(self.__dados)

    def __len__(self) -> int:
        return len(self.__dados)

    def elemento(self, posicao: int) -> Any:
        try:
            return self.__dados[posicao - 1]
        except IndexError:
            raise PilhaException(
                f'Posição inválida para a pilha atual com {len(self.__dados)} elementos.')

    def busca(self, conteudo: Any) -> int:
        for i in range(len(self.__dados)):
            if self.__dados[i] == conteudo:
                return i + 1
        raise PilhaException(f'Valor {conteudo} não está na pilha.')

    def modificar(self, posicao: int, conteudo: Any) -> None:
        try:
            self.__dados[posicao - 1] = conteudo
        except IndexError:
            raise PilhaException(
                f'Posição inválida para a pilha atual com {len(self.__dados)} elementos.')

    def empilha(self, conteudo: Any) -> None:
        self.__dados.append(conteudo)

    def desempilha(self) -> Any:
        if self.estaVazia():
            raise PilhaException('Pilha vazia')
        return self.__dados.pop()

    def __str__(self) -> str:
        s = ''
        for e in self.__dados:
            s += f'{e} '
        return s

    def esvazia(self):
        self.__dados.clear()
