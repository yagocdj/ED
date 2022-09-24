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
        return self.__start == None

    def tamanho(self) -> int:
        """
        # Percorre todos os nós de uma estrutura linear
        cont = 0
        cursor = self.__head
        while(cursor != None):
            cont += 1
            cursor = cursor.prox
        return cont
        """
        return self.__tamanho

    def __len__(self) -> int:
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
        cursor = self.__start
        cont = 0
        while(cursor != None):
            if cursor.carga == conteudo:
                return self.__tamanho - cont
            cont += 1
            cursor = cursor.prox
        raise PilhaException(f'Valor {conteudo} não está na pilha')

    def modificar(self, posicao: int, conteudo: Any):
        try:
            assert posicao > 0 and posicao <= self.__tamanho
            deslocamento = self.__tamanho - posicao

            cont = 0
            cursor = self.__start
            while(deslocamento > cont):
                cont += 1
                cursor = cursor.prox

            cursor.carga = conteudo
        except AssertionError:
            raise PilhaException(
                f'Posicao inválida para a pilha atual com {self.__tamanho} elementos')

    def empilha(self, conteudo: Any):
        novo = No(conteudo)
        novo.prox = self.__start
        self.__start = novo
        self.__tamanho += 1

    def desempilha(self) -> Any:
        if self.estaVazia():
            raise PilhaException(f'Pilha vazia.')
        carga = self.__start.carga
        self.__start = self.__start.prox
        self.__tamanho -= 1
        return carga

    def __str__(self):
        s = 'topo -> [ '
        cursor = self.__start
        while(cursor != None):
            s += f'{cursor.carga} '
            cursor = cursor.prox
        s += ' ]'
        return s

    def esvazia(self):
        #self.__start = None
        while(not self.estaVazia()):
            self.desempilha()
        # try:
        #    while(self.desempilha()):
        #        pass
        # except:
        #    pass

    def concatena(self, outraPilha: 'Pilha'):
        # Inverter a pilha "outraPilha"
        paux = Pilha()
        while(not outraPilha.estaVazia()):
            paux.empilha(outraPilha.desempilha())
        # descarregando paux na pilha que recebeu a chamada
        while(not paux.estaVazia()):
            self.empilha(paux.desempilha())

        """ 
        # utilizando o método inverte
        outraPilha.inverte()
        while (not outraPilha.estaVazia()):
            self.empilha(outraPilha.desempilha())
        """
