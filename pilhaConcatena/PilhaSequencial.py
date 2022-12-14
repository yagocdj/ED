class PilhaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Pilha:
    def __init__(self):
        self.__dados = list()

    def estaVazia(self)->bool:
        return len(self.__dados) == 0

    def tamanho(self)->int:
        return len(self.__dados)

    def __len__(self)->int:
        return len(self.__dados)

    def elemento(self, posicao:int)->any:
        try:
            return self.__dados[posicao-1]
        except IndexError:
            raise PilhaException(f'Posicao inválida para a pilha atual com {len(self.__dados)} elementos')
    
    def busca(self, conteudo:any)->int:
        for i in range(len(self.__dados)):
            if self.__dados[i] == conteudo:
                return i+1
        raise  PilhaException(f'Valor {conteudo} não está na pilha')

    def modificar(self, posicao:int, conteudo: any):
        try:
            self.__dados[posicao-1] = conteudo
        except IndexError:
            raise PilhaException(f'Posicao inválida para a pilha atual com {len(self.__dados)} elementos')

    def empilha(self, conteudo:any):
        self.__dados.append(conteudo)

    def desempilha(self)->any:
        if self.estaVazia():
            raise PilhaException(f'Pilha vazia.')
        return self.__dados.pop()

    def __str__(self):
        s = '[ '
        for e in self.__dados:
            s+=f'{e} '
        s += ' ] <- topo'
        return s

    def esvazia(self):
        self.__dados.clear()

    def concatena(self, outraPilha:'Pilha'):
        #Inverter a pilha "outraPilha"
        paux = Pilha()
        while(not outraPilha.estaVazia()):
            paux.empilha( outraPilha.desempilha())
        # descarregando paux na pilha que recebeu a chamada
        while(not paux.estaVazia()):
            self.empilha( paux.desempilha())






