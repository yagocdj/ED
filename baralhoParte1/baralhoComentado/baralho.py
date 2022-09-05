from carta import Carta
import random

class Baralho:
    def __init__(self):
        self.container = list()
        # variáveis locais (serão destruídas depois que o construtor terminar)
        naipe = ['ouro', 'espada', 'copa', 'paus']
        valor = ['As', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'valete', 'dama', 'rei']
        cor = ['vermelho', 'preto', 'vermelho', 'preto']

        # montando o baralho
        for n in range(len(naipe)):
            for v in range(len(valor)):
                self.container.append(Carta(valor[v], naipe[n], cor[n]))

    def __str__(self):
        s = ''
        for carta in self.container:
            s += (carta.__str__()) + '\n'
        return s

    # método especial length -> retornar o tamanho do baralho
    def __len__(self):
        return len(self.container)

    def embaralhar(self):
        random.shuffle(self.container)
