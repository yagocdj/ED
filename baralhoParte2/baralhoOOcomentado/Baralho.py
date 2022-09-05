from Carta import Carta
import random  # colocar os argumentos opcionais por último


class Baralho:  # type hint -> dica -> embaralhado:bool
    # valor default de embaralhar -> False
    def __init__(self, embaralhar: bool = False):
        # propriedade de instância -> self.propridedade -> estão imbutidas dentro de cada objeto
        self.__container = list()
        # não é interessante deixar os atributos públicos
        naipe = ['ouro', 'espada', 'copa', 'paus']
        cor = ['vermelho', 'preto', 'vermelho', 'preto']
        valor = ['As', '2', '3', '4', '5', '6', '7',
                 '8', '9', '10', 'valete', 'dama', 'rei']
        # método de instância -> podem ser utilizados quando o objeto é instanciado
        for n in range(len(naipe)):
            for v in range(len(valor)):
                self.__container.append(Carta(valor[v], naipe[n], cor[n]))

        if embaralhar:
            self.embaralhar()

    def __str__(self):
        s = ''
        for carta in self.__container:
            s += (carta.__str__() + '\n')
        return s

    def __len__(self):
        return len(self.__container)

    def embaralhar(self):
        random.shuffle(self.__container)

    def retirarCarta(self) -> Carta:  # dica do que esse método retorna (Carta)
        return self.__container.pop()  # o pop é uma pilha -> o final da lista é o topo

    def temCarta(self) -> bool:
        if len(self.__container) == 0:
            return False
        else:
            return True

    def receberCarta(self, carta: Carta) -> bool:
        if carta not in self.__container:
            self.__container.append(carta)
            return True
        return False

    def juntarBaralho(self, outroBaralho):
        for i in range(len(outroBaralho)):
            carta_retirada = outroBaralho.retirarCarta()
            # o receberCarta já faz tudo internamente
            if not self.receberCarta(carta_retirada):
                outroBaralho.receberCarta(carta_retirada)
