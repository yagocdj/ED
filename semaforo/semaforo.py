import time


class Semaforo:
    def __init__(self, tempoVermelho: int, tempoVerde: int, tempoAmarelo: int, estadoInicial: int):
        self.__luzes = ('verde', 'amarelo', 'vermelho')
        self.__timerVermelho = tempoVermelho
        self.__timerVerde = tempoVerde
        self.__timerAmarelo = tempoAmarelo
        # quem programa o sinal escolhe o estado inicial dele
        # 0 -> verde; 1 -> amarelo; 2 -> vermelho
        self.__estadoAtual = self.__luzes[estadoInicial]

    def mudarEstadoAtual(self) -> None:
        if self.__estadoAtual == 'vermelho':
            self.__estadoAtual = self.__luzes[0]  # set to 'verde'
        elif self.__estadoAtual == 'amarelo':
            self.__estadoAtual = self.__luzes[2]  # set to 'vermelho'
        else:
            self.__estadoAtual = self.__luzes[1]  # set to 'vermelho'

    def contagemRegressiva(self) -> None:
        if self.__estadoAtual == 'vermelho':
            tempo = self.__timerVermelho
        elif self.__estadoAtual == 'amarelo':
            tempo = self.__timerAmarelo
        else:
            tempo = self.__timerVerde
        while tempo:
            secs = tempo
            timer = f'Timer: {secs:02d}'
            print(timer, end='\r')
            time.sleep(1)
            tempo -= 1

    def setTempoTransicao(self, novoTempoVermelho: int, novoTempoAmarelo: int, novoTempoVerde: int) -> None:
        self.__timerVermelho = novoTempoVermelho
        self.__timerAmarelo = novoTempoAmarelo
        self.__timerVerde = novoTempoVerde

    def exibirEstadoAtual(self) -> None:
        if self.__estadoAtual == 'vermelho':
            print('\nSinal \033[91m{}\033[00m'.format(
                self.__estadoAtual))
        elif self.__estadoAtual == 'verde':
            print('\nSinal \033[92m{}\033[00m'.format(
                self.__estadoAtual))
        else:
            print('\nSinal \033[93m{}\033[00m'.format(
                self.__estadoAtual))
