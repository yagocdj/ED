from typing import Any


class PilhaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class No:
    def __init__(self, carga: Any):
        self.carga = carga
        self.prox = None

    def __str__(self):
        return str(self.carga)


class Pilha:
    def __init__(self):
        self.__start = None
        self.__tamanho = 0

    def estaVazia(self) -> bool:
        return self.__start is None

    def tamanho(self) -> int:
        '''
        # Percorre todos os nós de uma estrutura linear
        cont = 0
        cursor = self.__head
        while(cursor != None):
            cont += 1
            cursor = cursor.prox
        return cont
        '''
        cont = 0
        cursor = self.__start
        while (cursor is not None):
            cont += 1
            cursor = cursor.prox
        self.__tamanho = cont
        return self.__tamanho

    def __len__(self) -> int:  # len(Pilha()) -> self.__tamanho
        return self.__tamanho

    def elemento(self, posicao: int) -> Any:
        '''
        Retorna a carga armazenada no nó indicado por "posicao"
        '''
        try:
            assert posicao > 0 and posicao <= self.__tamanho
            deslocamento = self.__tamanho - posicao

            cont = 0
            cursor = self.__start
            while(deslocamento > cont):
                cont += 1
                cursor = cursor.prox

            return cursor.carga
        except AssertionError:
            raise PilhaException(
                f'Posicao inválida para a pilha atual com {self.__tamanho} elementos')

    def busca(self, conteudo: Any) -> int:
        '''
        Retorna a posição do nó cuja carga é igual a "conteudo"
        '''
        cursor = self.__start
        cont = 0
        while(cursor is not None):
            if cursor.carga == conteudo:
                return self.__tamanho - cont
            cont += 1
            cursor = cursor.prox
        raise PilhaException(f'Valor {conteudo} não está na pilha')

    def modificar(self, posicao: int, conteudo: Any):  # modificar o conteúdo de uma posição
        """
        try:
            self.__dados[posicao-1] = conteudo
        except IndexError:
            raise PilhaException(
                f'Posicao inválida para a pilha atual com {len(self.__dados)} elementos')
        """
        try:
            assert posicao > 0 and posicao <= self.__tamanho
            deslocamento = self.__tamanho - posicao

            cont = 0
            cursor = self.__start
            while (deslocamento > cont):
                cont += 1
                cursor = cursor.prox
            cursor.carga = conteudo
        except AssertionError:
            raise PilhaException(
                f'Posicao inválida para a pilha atual com {self.__tamanho} elementos')

    def empilha(self, conteudo: Any):
        pass
            # self.__dados.append(conteudo)

    def desempilha(self) -> Any:
        pass
        """
        if self.estaVazia():
            raise PilhaException(f'Pilha vazia.')
        return self.__dados.pop()
        """

    def __str__(self):
        s = ''
        cont = 0
        cursor = self.__start
        while (cursor is not None):
            cont += 1
            cursor = cursor.prox
            s += f'{cursor.carga} '
        return s

    def esvazia(self):
        self.__dados.clear()


if __name__ == "__main__":
    p1 = Pilha()

    p1.empilha(10)
    print(p1)
